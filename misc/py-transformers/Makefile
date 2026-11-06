# hlab overlay override: stock misc/py-transformers (5.3.0) hard-wires the
# whole pytorch ecosystem (torch, torchvision, torchaudio, accelerate,
# sagemaker, timm) as RUN_DEPENDS. AudioMuse-AI pins transformers==4.57.6
# and its Docker runtime image contains NONE of the torch stack (see
# upstream requirements/common.txt + Dockerfile). PORTEPOCH keeps ours
# winning over the stock port while this override is needed; retire when
# the stock port slims its deps.

PORTNAME=	transformers
PORTVERSION=	4.57.6
PORTEPOCH=	1
CATEGORIES=	misc python # machine-learning
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	e4779@4779.ru
COMMENT=	State-of-the-art machine learning for JAX, PyTorch and TensorFlow (slim)
WWW=		https://github.com/huggingface/transformers

LICENSE=	APACHE20

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}setuptools>=61:devel/py-setuptools@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}wheel>0:devel/py-wheel@${PY_FLAVOR}

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}filelock>0:sysutils/py-filelock@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}huggingface-hub>=0.34.0:misc/py-huggingface-hub@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}numpy>=1.17:math/py-numpy@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}packaging>0:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}pyyaml>=5.1:devel/py-pyyaml@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}regex>0:textproc/py-regex@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}tokenizers>=0.22.0<0.24:textproc/py-tokenizers@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}safetensors>=0.4.3:misc/py-safetensors@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}tqdm>=4.27:misc/py-tqdm@${PY_FLAVOR}

USES=		python
USE_PYTHON=	autoplist pep517

.include <bsd.port.mk>
