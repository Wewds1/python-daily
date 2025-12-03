import cv2
import imageio
import random
import string
import numpy as np

# image = cv2.imread("sample.png ")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, shadow = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)


# cv2.imwrite("shadow.png", shadow)


def image_to_text(image, text, out="output.png"):
    image = cv2.imread(image)
    h,w = image.shape[:2]

    # print(h,w)


    # Create a blank mask
    mask = np.zeros((h,w), dtype=np.uint8)
    cv2.putText(mask, text, (w//2-10, h//2), cv2.FONT_HERSHEY_SIMPLEX, 3, (255), 5, cv2.LINE_AA)

    # Create Output Canvas
    output = np.zeros_like(image)


    # Fill text Pixesl with image pixels
    y_indices, x_indices = np.where(mask > 0)
    for y, x in zip(y_indices, x_indices):
        output[y, x] = image[y, x]

    cv2.imwrite(out, output)


def morph_image(A_path, B_path, out="morphed.png"):
    A = cv2.imread(A_path)
    B = cv2.imread(B_path)

    #Set custom size as for mine i want 600x600 only
    h, w = 600, 600

    # Resize both image to the same size
    A = cv2.resize(A, (w, h))
    B_gray = cv2.cvtColor(cv2.resize(B, (w, h)), cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(B_gray, 125, 255, cv2.THRESH_BINARY)


    output = np.zeros_like(A)

    yA, xA = np.where(thresh > 0)
    yB, xB = yA.copy(), xA.copy()


    np.random.shuffle(yA)
    np.random.shuffle(xA)

    for ya, xa, yb, xb in zip(yA, xA, yB, xB):
        output[yb, xb] = A[ya, xa]

    cv2.imwrite(out, output)


def matrix_effect(input_path, output = "matrix_effect.png"):
    img = cv2.imread(input_path)

    green = img.copy()
    green[:, :, 0] = 0 #remove blue channel
    green[:, :, 2] = 0 #rmove red channgeel

    green = cv2.GaussianBlur(green, (9,9), 0)

    cv2.imwrite(output, green)
    return output


def matrix_rain_effect(input_path, output="matrix_rain_effect.png"):
    img = cv2.imread(input_path)
    h, w = img.shape[:2]

    green = img.copy()
    green [:, :, 0] = 0 #remove blue channel
    green [:, :, 2] = 0 #remove red channel


    green = cv2.GaussianBlur(green, (9,9), 0)

    overlay = np.zeros_like(green)

    font = cv2.FONT_HERSHEY_COMPLEX

    for x in range(0, w, 20): # get w coordinates 
        for y in range(0, h, 20): #get h coordinates
            # Generate random ASCII character then spread iwht h and w
            char = chr(np.random.randint(33, 126))
            cv2.putText(overlay, char, (x, y), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

    # add weight to make font visible
    out = cv2.addWeighted(green, 0.7, overlay, 0.3, 0)
    cv2.imwrite(output, out)
    return output


def disintegrate_effect(input_path, output="disintegrate_effect.gif", block_size=2, frames=40):
    img = cv2.imread(input_path)
    h, w = img.shape[:2]

    particles = []

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            #Get block from 0-2 pixels so 2x2 (x, y)
            block = img[y:y+block_size, x:x+block_size].copy()
            #Note initial position
            px = x
            py = y

            #add random velocity for each block
            vx = random.uniform(-1.5, 1.5)
            vy = random.uniform(-1, -3.0)


            particles.append([px, py, block, vx, vy])

    gif_frames = []

    for frame in range(frames):
        canvas = np.zeros_like(img)

        for p in particles:
            px, py, block, vx, vy = p


            vy += 0.3 #gravity effect of falling down eme

            #Update position
            px += vx
            py += vy

            p[0] = px
            p[1] = py
            p[3] = vy

            #draw block if within bounds
            ix, iy = int(px), int(py)
            if 0 <= ix < w-block_size and 0 <= iy < h-block_size:
                canvas[iy:iy+block_size, ix:ix+block_size] = block
            
        gif_frames.append(canvas)

    imageio.mimsave(output, gif_frames, fps=10)
    return output



def particle_transform(input_image, output_gif="particle_transform.gif", block_size=2, form_frames=80,
                       gravity = 0.1, explode_strength=5.0, disintegrate_frames=60, text=None, text_scale=3,
                       text_thickness=5, random_text_length=(4,8)):
    

    img = cv2.imread(input_image)
    h, w = img.shape[:2]

    #as usual create list to store particles
    particles = []

    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            block = img[y:y+block_size, x:x+block_size].copy()
            px = x 
            py = y

            vx = random.uniform(-explode_strength, explode_strength)
            vy = random.uniform(-explode_strength*0.7, explode_strength*1.2)


            particles.append([px, py, vx, vy, block])
    
    #add list for frames in disintegrate effect
    frames_list = []

    for frame in range(form_frames):
        canvas = np.zeros_like(img)

        for p in particles:
            px, py, vx, vy, block = p

            vy += gravity

            px += vx
            py += vy

            p[0] = px
            p[1] = py
            p[4] = vy

            ix, iy = int(px), int(py)
            if 0 <= ix < w-block_size and 0 <= iy < h-block_size:
                canvas[iy:iy+block_size, ix:ix+block_size] = block

        frames_list.append(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))

    if text is None: 
        min_len, max_len = random_text_length
        word_len = random.randint(min_len, max_len)
        text = "".join(random.choices(string.ascii_uppercase) for _ in range(word_len))

    print("Formatting Text:", text)

    mask = np.zeros((h,w), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, text_scale, text_thickness)[0]

    tx = (w - text_size[0]) // 2
    ty = (h + text_size[1]) // 2

    cv2.putText(mask, text, (tx, ty), font, text_scale, (255), text_thickness, cv2.LINE_AA)

    ys, xs = np.where(mask == 255)
    targets = list(zip(xs, ys))

    random.shuffle(targets)

    targets = targets[:len(particles)]
    while len(targets) < len(particles):
        targets.append(random.choice(targets))

    for p,t in zip(particles, targets):
        p.append(t)


    # Form the Text


    for frame in range(form_frames):
        canvas = np.zeros_like(img)

        for p in particles:
            px, py, vx, vy, block, target = p
            tx, ty = target

            px += (tx - px) * 0.2
            py += (ty - py) * 0.2

            p[0] = px
            p[1] = py

            ix, iy = int(px), int(py)
            if 0 <= ix < w-block_size and 0 <= iy < h-block_size:
                canvas[iy:iy+block_size, ix:ix+block_size] = block
        frames_list.append(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))

    imageio.mimsave(output_gif, frames_list, fps=15)
    print("Saved GIF as:", output_gif)
    return output_gif




# print(morph_image("sample.png", "img.jpg"))
# print(image_to_text("sample.png", "Hello World"))
# print(matrix_effect("sample.png"))
# print(matrix_rain_effect("sample.png"))
# print(disintegrate_effect("sample.png"))
print(particle_transform("bebe.jpeg", text="I LOVE YOU"))






