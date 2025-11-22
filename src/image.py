from PIL import Image
import shutil
import os
import json

# Desired sizes
icon_sizes = [16, 24, 32, 48, 64, 96, 128, 256, 512]

def create_icons(input_png, output_folder='output_icons'):
    # Load the original image
    original = Image.open(input_png).convert("RGBA")

    os.makedirs(output_folder, exist_ok=True)

    for size in icon_sizes:
        # Resize to square icon
        resized = original.resize((size, size), Image.LANCZOS)

        # Save as PNG
        png_path = os.path.join(output_folder, f'{size}x{size}.png')
        resized.save(png_path, format='PNG')
        print(f'Saved PNG: {png_path}')

        # Save as ICO (single size per file)
        ico_path = os.path.join(output_folder, f'{size}x{size}.ico')
        resized.save(ico_path, format='ICO', sizes=[(size, size)])
        print(f'Saved ICO: {ico_path}')

def create_icons_main(input_png, output_folder='output_icons'):
    # Load the original image
    original = Image.open(input_png).convert("RGBA")

    os.makedirs(output_folder, exist_ok=True)

    for size in [512]:
        # Resize to square icon
        resized = original.resize((size, size), Image.LANCZOS)

        # Save as PNG
        png_path = os.path.join(output_folder, f'icon.png')
        resized.save(png_path, format='PNG')
        print(f'Saved PNG: {png_path}')

        # Save as ICO (single size per file)
        ico_path = os.path.join(output_folder, f'{size}x{size}.ico')
        resized.save(ico_path, format='ICO', sizes=[(size, size)])
        print(f'Saved ICO: {ico_path}')


def copy_launcher_folders(images_dir, android_res_path):
    for folder in os.listdir(images_dir):
        src = os.path.join(images_dir, folder)
        dst = os.path.join(android_res_path, folder)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
            print(f"Copied {src} to {dst}")

def copy_icon_files(src_dir, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    for file in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(dst_dir, file)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)
            print(f"Copied {src_file} to {dst_file}")

def read_copy_update():
    create_icons('logo.DGIlOnDO-9.png')
    create_icons_main('logo.DGIlOnDO-9.png')
    copy_icon_files("output_icons", "../src-tauri/icons/")

    # Update tauri.conf.json icon paths
    tauri_conf_path = '../src-tauri/tauri.conf.json'
    with open(tauri_conf_path, 'r', encoding='utf-8') as f:
        conf = json.load(f)

    # Update icon paths to output_icons
    if 'bundle' in conf and 'icon' in conf['bundle']:
        conf['bundle']['icon'] = [f"icons/{os.path.basename(path)}" for path in os.listdir("../src-tauri/icons/") if path.endswith('.png') or path.endswith('.ico')]

    with open(tauri_conf_path, 'w', encoding='utf-8') as f:
        json.dump(conf, f, indent=2)
    print(f"Updated icon paths in {tauri_conf_path}")



def copy_move():
    copy_launcher_folders("andriod", "../src-tauri/gen/android/app/src/main/res/")
    read_copy_update()

if __name__ == "__main__":
    # Change 'input.png' to your source image file name
    copy_move()
