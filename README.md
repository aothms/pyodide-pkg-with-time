# pyodide-pkg-with-time

```
mkdir build && cd build
git clone https://github.com/aothms/pyodide-pkg-with-time
git clone https://github.com/pyodide/pyodide
pyodide/run_docker

cd pyodide
make
pip install ./pyodide-build
cd ..

cd pyodide-pkg-with-time
PYODIDE_ROOT=/src/pyodide \
PATH=/src/pyodide/emsdk/emsdk:/src/pyodide/emsdk/emsdk/node/14.18.2_64bit/bin:/src/pyodide/emsdk/emsdk/upstream/emscripten:$PATH \
python -m pyodide_build buildpkg simple.yml

python -m http.server
```
