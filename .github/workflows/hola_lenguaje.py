name: Hola Lenguaje
run-name: Creando Hola Lenguaje
on: [push]
jobs:
  holamundo:
    runs-on: ubuntu-latest
    steps:
       - name: Checkout
          uses: actions/checkout@v3
        - name: Definir nombre
          run: echo "USERNAME=${{ inputs.nombre }}" >> $GITHUB_ENV
        - name: Definir lenguaje
          run: echo "LANGUAGE=${{ inputs.lenguaje_favorito }}" >> $GITHUB_ENV
        - name: Correr script
          run: python hola_lenguaje.py
