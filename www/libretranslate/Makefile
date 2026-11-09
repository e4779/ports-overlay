# hlab overlay: LibreTranslate API server — MT backend for SillyTavern
# translation (runbook 27/28). Absent from tree 2026-11-09.
#
# Version drift (accepted, audiomuse precedent): upstream pins
# Flask==2.2.5 / Werkzeug==2.3.8 / Flask-Babel==3.1.0 / Flask-Limiter==2.6.3
# / numpy<2(py3.12); tree ships Flask 3.x / Werkzeug 3.x / Babel 4.x /
# Limiter 3.x / numpy 2.x. Smoke-tested at deploy; if the app breaks on
# Flask 3, fallback = pinned mini-ports (see runbook 28).

PORTNAME=	libretranslate
DISTVERSION=	1.9.6
PORTREVISION=	1
CATEGORIES=	www python # machine-learning
MASTER_SITES=	PYPI

MAINTAINER=	e4779@4779.ru
COMMENT=	Self-hosted machine translation API (argos-translate, CPU)
WWW=		https://libretranslate.com

LICENSE=	AGPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}hatchling>0:devel/py-hatchling@${PY_FLAVOR}

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}flask>=0:www/py-flask@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}werkzeug>=0:www/py-werkzeug@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}itsdangerous>=0:security/py-itsdangerous@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}flask-babel>=0:devel/py-flask-babel@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}flask_limiter>=0:www/py-flask-limiter@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}flask-swagger>=0.2.14:www/py-flask-swagger@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}flask-swagger-ui>=4.11.1:www/py-flask-swagger-ui@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}waitress>=0:www/py-waitress@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}expiringdict>=0:devel/py-expiringdict@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}langdetect>=0:textproc/py-langdetect@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}lexilang>=1.0:devel/py-lexilang@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}APScheduler>=0:devel/py-apscheduler@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}redis>=0:databases/py-redis@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}numpy>=0:math/py-numpy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}prometheus-client>=0:net-mgmt/py-prometheus-client@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}polib>=0:devel/py-polib@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}packaging>=0:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}argos-translate-lt>=1.12.1:textproc/py-argos-translate-lt@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}argos-translate-files>=1.4.4:textproc/py-argos-translate-files@${PY_FLAVOR}

USES=		python:3.10+
USE_PYTHON=	autoplist pep517
NO_ARCH=	yes

USE_RC_SUBR=	libretranslate

.include <bsd.port.mk>
