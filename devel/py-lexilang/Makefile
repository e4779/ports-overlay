# hlab overlay: dep of LibreTranslate (runbook 28); pure python,
# absent from tree 2026-11-09. License per PyPI metadata.
# Sdist is LEGACY setup.py (no pyproject) — build backend
# setuptools.build_meta:__legacy__, hence setuptools in BUILD_DEPENDS.

PORTNAME=	lexilang
PORTVERSION=	1.0.7
CATEGORIES=	devel python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Fast lexical language identification
WWW=		https://pypi.org/project/lexilang/

LICENSE=	AGPLv3

NO_ARCH=	yes
USES=		python:3.10+
USE_PYTHON=	autoplist pep517


BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

.include <bsd.port.mk>
