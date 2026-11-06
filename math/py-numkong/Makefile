# hlab overlay mini-port: runtime dep of audio/audiomuse-ai (IVF quantization,
# tasks/ivf_quant.py; upstream pin numkong==7.7.0).

PORTNAME=	numkong
PORTVERSION=	7.7.0
CATEGORIES=	math python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	Portable mixed-precision math and linear-algebra library with SIMD kernels
WWW=		https://github.com/ashvardanian/NumKong

LICENSE=	APACHE20

USES=		python
USE_PYTHON=	autoplist pep517

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

.include <bsd.port.mk>
