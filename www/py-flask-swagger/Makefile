# hlab overlay: dep of www/libretranslate (runbook 28); absent from tree
# 2026-11-09. Pure python.

PORTNAME=	flask-swagger
PORTVERSION=	0.2.14
CATEGORIES=	www python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Extract swagger specs from Flask routes
WWW=		https://github.com/gangverk/flask-swagger

LICENSE=	MIT

NO_ARCH=	yes
USES=		python:3.10+
USE_PYTHON=	autoplist pep517

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}flask>=0:www/py-flask@${PY_FLAVOR}

.include <bsd.port.mk>
