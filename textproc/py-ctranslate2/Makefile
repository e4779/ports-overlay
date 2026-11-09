# hlab overlay: python bindings for CTranslate2 (runbook 28, LibreTranslate
# chain). Upstream ships no PyPI sdist (wheels only) — build from the same
# GH tag as textproc/ctranslate2. Links the shared lib installed by that
# port via CTRANSLATE2_ROOT (see python/setup.py upstream).
# Upstream build-system pins pybind11==2.13.6 — tree version accepted
# (API stable across 2.13/2.14), drift documented here.

PORTNAME=	ctranslate2
DISTVERSIONPREFIX=	v
DISTVERSION=	4.8.5
CATEGORIES=	textproc python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Python bindings for the CTranslate2 inference engine
WWW=		https://github.com/OpenNMT/CTranslate2

LICENSE=	MIT

USE_GITHUB=	yes
GH_ACCOUNT=	OpenNMT
GH_PROJECT=	CTranslate2
WRKSRC_SUBDIR=	python

LIB_DEPENDS=	libctranslate2.so:textproc/ctranslate2

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pybind11>=2.13:devel/py-pybind11@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

USES=		python:3.10+
USE_PYTHON=	autoplist pep517

MAKE_ENV+=	CTRANSLATE2_ROOT=${LOCALBASE}

.include <bsd.port.mk>
