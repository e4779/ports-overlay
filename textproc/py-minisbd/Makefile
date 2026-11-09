# hlab overlay: dep of argos-translate-lt (LibreTranslate chain, runbook 28);
# pure python, absent from tree 2026-11-09. License per PyPI metadata.
# Sdist is hatchling-built: BUILD_DEPENDS carries py-hatchling.

PORTNAME=	minisbd
PORTVERSION=	0.9.5
CATEGORIES=	textproc python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Minimal rule-based sentence boundary detection
WWW=		https://pypi.org/project/minisbd/

LICENSE=	AGPLv3

NO_ARCH=	yes
USES=		python:3.10+
USE_PYTHON=	autoplist pep517

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}hatchling>0:devel/py-hatchling@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

.include <bsd.port.mk>
