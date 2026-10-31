# Efface un faux logo généré par l'IA sur un objet du décor (ici un sac cadeau) (reconstruction OpenCV), image par image.
# Les pixels rouges du logo sont repérés dans une zone de recherche, dilatés, puis reconstruits à partir du sac autour.
# Usage : python effacer-logo.py entree.mp4 sortie.mp4 debut_s  (régler X0, X1, Y0, Y1 sur la zone du logo ; demande opencv-python-headless)
import sys, subprocess, numpy as np, cv2

src, dst, t0 = sys.argv[1], sys.argv[2], float(sys.argv[3])
W, H, FPS = 720, 1280, 30
X0, X1, Y0, Y1 = 0, 320, 840, 1120          # zone où se trouve le logo du sac

dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', src, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-i', src, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium',
                        '-pix_fmt', 'yuv420p', '-c:a', 'copy', dst], stdin=subprocess.PIPE)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
n = done = 0
while True:
    buf = dec.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: break
    fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
    if n / FPS >= t0:
        z = fr[Y0:Y1, X0:X1].astype(int)
        strong = (z[..., 0] > 120) & (z[..., 1] < 150) & (z[..., 0] - z[..., 1] > 45)
        if strong.sum() > 40:
            # autour du logo seulement : on prend aussi les traits fins rose pâle (anti-crénelage)
            ys, xs = np.nonzero(strong); pad = 25
            bx0, bx1 = max(0, xs.min() - pad), min(z.shape[1], xs.max() + pad); by0, by1 = max(0, ys.min() - pad), min(z.shape[0], ys.max() + pad)
            weak = np.zeros_like(strong); zz = z[by0:by1, bx0:bx1]
            ref = np.median(zz.reshape(-1, 3), axis=0).max()  # blanc du sac
            weak[by0:by1, bx0:bx1] = ((zz[..., 0] - zz[..., 1] > 12) & (zz[..., 0] > 110)) | (zz.max(axis=2) < ref - 22)
            m = cv2.dilate(((strong | weak) * 255).astype(np.uint8), kernel, iterations=2)
            full = np.zeros((H, W), np.uint8); full[Y0:Y1, X0:X1] = m
            fr = cv2.inpaint(fr, full, 9, cv2.INPAINT_TELEA); done += 1
    enc.stdin.write(fr.tobytes()); n += 1
enc.stdin.close(); enc.wait()
print(f'{n} images, logo effacé sur {done}')
