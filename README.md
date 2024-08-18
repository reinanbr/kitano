<h1 align='center'>Kitano</h1>
<p align='center'>
<!-- 
<img height='200px' width='200px' src='https://raw.githubusercontent.com/gpftc/covid_br/main/covidbr/img/covidbr_logo.png'> -->
<br/>
<a href="https://github.com/reinanbr"><img title="Autor" src="https://img.shields.io/badge/Autor-reinan_br-blue.svg?style=for-the-badge&logo=github"></a>
<br/>

<p align='center'>

<!-- outros premios e analises -->
<a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/reinanbr/kitano?logo=codefactor"></a>
<br/>
<!-- github dados -->
<!--<a href='https://python.org'><img src='https://img.shields.io/github/poetry/locked/python-version/reinanbr/kitano'></a>-->
<a href='#'><img src='https://img.shields.io/github/languages/code-size/reinanbr/kitano'></a>
<a href='#'><img src='https://img.shields.io/github/commit-activity/m/reinanbr/kitano'></a>
<a href='#'><img src='https://img.shields.io/github/last-commit/reinanbr/kitano'></a>
<br/>
<!-- sites de pacotes -->
<a href='https://pypi.org/project/kitano/'><img src='https://img.shields.io/pypi/v/kitano'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/kitano'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/kitano"></a>
<a href='#'><img src='https://img.shields.io/pypi/implementation/kitano'></a>
<br/>
<!-- redes sociais -->
<br/>
<a href='https://instagram.com/gpftc_ifsfertao/'><img src='https://shields.io/badge/insta-gpftc_ifsertao-violet?logo=instagram&style=flat'></a>
</p>
</p>
<p align='center'> <b>Library for working and development in python</b></p>
<hr/>

## Installation

```bash
$ pip install kitano -U
```

<hr>
<br>

## Examples

### printing

```py
from kitano.logging import puts
import kitano.logging as logg

strf = logg.strft

print(strf)

logg.str_date(strf)

puts('testing...',file_log='app.log')

```
result:
```sh

[%d/%m/%Y %H:%M:%S]:
[01/01/2023 22:48:06]: testing... 
```
