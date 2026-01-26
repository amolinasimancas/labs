## Principales comandos de anaconda
A continuación se listan los comandos más comunes a tener en cuenta en la gestión de entornos virtuales con anaconda:

```sh
conda init # ~/anaconda3/bin/conda init
jupyter-notebook # correr jupyter notebook localhost
conda env list # listar entornos
conda create --name nombre_entorno python=3.5 pandas # crear entorno
conda activate nombre_entorno # activar entorno
conda deactivate # desactivar entorno
conda list # listar paquetes
conda install nombre_paquete
conda remove nombre_paquete
conda env remove --name nombre_entorno
conda env export --from-history --file environment.yml
conda env create --file environment.yml

```