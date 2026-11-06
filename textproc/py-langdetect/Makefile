# hlab overlay mini-port: runtime dep of audio/audiomuse-ai (lazy import in
# lyrics/lyrics_transcriber.py; upstream pin langdetect==1.0.9).

PORTNAME=	langdetect
PORTVERSION=	1.0.9
CATEGORIES=	textproc python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Language detection library ported from Google's language-detection
WWW=		https://github.com/Mimino666/langdetect

LICENSE=	MIT

USES=		python
USE_PYTHON=	autoplist distutils

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}six>0:devel/py-six@${PY_FLAVOR}

.include <bsd.port.mk>
