# hlab overlay mini-port: runtime dep of audio/audiomuse-ai (WordNet synonyms
# for mood vocab, tasks/ai/vocab.py; upstream pin wn==0.13.0).

PORTNAME=	wn
PORTVERSION=	0.13.0
CATEGORIES=	textproc python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Wordnet interface library
WWW=		https://github.com/goodmami/wn

LICENSE=	MIT

USES=		python
USE_PYTHON=	autoplist pep517

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}hatchling>0:devel/py-hatchling@${PY_FLAVOR}
RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}httpx>0:www/py-httpx@${PY_FLAVOR}

.include <bsd.port.mk>
