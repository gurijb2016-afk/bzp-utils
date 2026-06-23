import os

pkg_name = "bzipmini"
version = "1.0"
desc = "Simple LZ77 folder archiver in Python"
license_type = "MIT"

content = f"""
pkgname={pkg_name}
pkgver={version}
pkgrel=1
pkgdesc="{desc}"
arch=('any')
license=('{license_type}')
depends=('python')

source=("cli.py" "lz77.py")

package() {{
    install -Dm755 cli.py "$pkgdir/usr/bin/bzp"
    install -Dm644 lz77.py "$pkgdir/usr/lib/{pkg_name}/lz77.py"
}}
"""

with open("PKGBUILD", "w") as f:
    f.write(content.strip() + "\n")

print("PKGBUILD generated successfully")
