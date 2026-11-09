# hlab overlay: file-translation plugin pinned by www/libretranslate 1.9.6
# (runbook 28). PyPI dist 1.4.4 has NO sdist (wheel-only) — source is the
# LibreTranslate fork; upstream argosopentech repo tags stop at v1.1.3.
# Drift: upstream pins beautifulsoup4==4.9.3 — tree version accepted
# (house precedent, audiomuse runbook 26).

PORTNAME=	argos-translate-files
DISTVERSIONPREFIX=	v
DISTVERSION=	1.4.4
CATEGORIES=	textproc python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Translate files (docx/pdf/srt/…) with Argos Translate
WWW=		https://github.com/LibreTranslate/argos-translate-files

LICENSE=	MIT

USE_GITHUB=	yes
GH_ACCOUNT=	LibreTranslate

NO_ARCH=	yes
USES=		python:3.10+
USE_PYTHON=	autoplist pep517

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}argos-translate-lt>=1.12.1:textproc/py-argos-translate-lt@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}beautifulsoup4>=4.9:www/py-beautifulsoup4@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}lxml>=4.9:devel/py-lxml@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pysrt>=1.1:textproc/py-pysrt@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pymupdf>=1.24:print/py-PyMuPDF@${PY_FLAVOR}

.include <bsd.port.mk>
