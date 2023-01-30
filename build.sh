pip uninstall zdppy_requests -y
rm -rf dist
poetry build
pip install dist/zdppy_requests-0.1.3-py3-none-any.whl