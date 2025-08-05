from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='diagnostico_cancer_ml',
    version='1.0.0',
    packages=find_packages(),
    description='Pacote Python para análise de exames médicos usando Machine Learning',
    author='Vinicius Aragão',
    author_email='cont.viniciusaragao@gmail.com',
    url='https://github.com/vinicius025/diagnostico_cancer_ml.git',  
    license='Creative Commons Attribution 4.0 International (CC BY 4.0)',  
    long_description=long_description,
    long_description_content_type='text/markdown'    
)
