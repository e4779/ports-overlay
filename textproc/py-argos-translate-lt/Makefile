# hlab overlay: LibreTranslate's argos-translate fork (PyPI dist
# argos-translate-lt), pinned by www/libretranslate 1.9.6. Absent from tree
# 2026-11-09. Source = GitHub tag, NOT PyPI sdist: the sdist is broken
# (setup.py reads requirements.txt which is missing from the sdist —
# MANIFEST bug upstream). Deps per PyPI metadata; the fork drops upstream's
# heavy spacy/stanza chain (sentence splitting via minisbd) — that is WHY
# the fork, not stock argostranslate.

PORTNAME=	argos-translate-lt
DISTVERSIONPREFIX=	v
DISTVERSION=	1.12.1
CATEGORIES=	textproc python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Argos Translate (LibreTranslate fork) — offline neural MT library
WWW=		https://github.com/LibreTranslate/argos-translate

LICENSE=	MIT

USE_GITHUB=	yes
GH_ACCOUNT=	LibreTranslate
GH_PROJECT=	argos-translate

NO_ARCH=	yes
USES=		python:3.10+
USE_PYTHON=	autoplist pep517

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}ctranslate2>=4.0:textproc/py-ctranslate2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}sentencepiece>=0.2.0:textproc/py-sentencepiece@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}packaging>=0:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}sacremoses>=0.0.53:textproc/py-sacremoses@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}minisbd>=0.9:textproc/py-minisbd@${PY_FLAVOR}

.include <bsd.port.mk>
