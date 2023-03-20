from setuptools import setup, find_packages


if __name__=='__main__':
    setup(
        name='ldm',
        version='1.0.0',
        description='Latent diffusion models',
        packages=find_packages(exclude=('test',)),
        install_requires=[
            'torch',
            'numpy',
            'tqdm',
        ],
    )