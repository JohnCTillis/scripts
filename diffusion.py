#!/usr/bin/env python
import urllib.request
import replicate
import os


os.environ["REPLICATE_API_TOKEN"] = "<YOUR_SECRET_API_KEY>"

model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1")

# https://replicate.com/stability-ai/stable-diffusion/versions/f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1#input
prompt: str = str(input("Enter stable-diffusion prompt...\n"))
inputs = {
    # Input prompt
    'prompt': prompt,

    # Specify things to not see in the output
    # 'negative_prompt': ...,

    # Width of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'width': 768,

    # Height of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'height': 768,

    # Prompt strength when using init image. 1.0 corresponds to full
    # destruction of information in init image
    'prompt_strength': 0.8,

    # Number of images to output.
    # Range: 1 to 4
    'num_outputs': 1,

    # Number of denoising steps
    # Range: 1 to 500
    'num_inference_steps': 50,

    # Scale for classifier-free guidance
    # Range: 1 to 20
    'guidance_scale': 7.5,

    # Choose a scheduler.
    'scheduler': "DPMSolverMultistep",

    # Random seed. Leave blank to randomize the seed
    # 'seed': ...,
}

# https://replicate.com/stability-ai/stable-diffusion/versions/f178fa7a1ae43a9a9af01b833b9d2ecf97b1bcb0acfd2dc5dd04895e042863f1#output-schema
output = version.predict(**inputs)
print(output)
def main():
    inp = input("Would you like to download the image? (y/n)")
    if inp == "y":
        url = output[0]
        filename = 'out-0.png'
        urllib.request.urlretrieve(url, filename)
    elif inp == "n":
        print("Ok boss, gotcha")
    else:
        print("Not an option... Try again...")
        main()

if __name__ == "__main__":
    main()
