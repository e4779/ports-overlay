# hlab overlay: AudioMuse-AI native CPU port (runbook 26, Phase 1).
# WHY: no port exists anywhere (repology empty 2026-11-06); CPU baseline —
# Flask + taskqueue workers over pkg python deps. GPU path is the podman
# worker (Phase 2), NOT this package. Dep versions drift vs
# requirements/common.txt pins (documented in runbook 26); many pins match
# exactly. stopwords from common.txt is NOT imported anywhere — skipped.
# pgserver/waitress/pyinstaller are Linux-native build deps — skipped.
# Retire this overlay port when an official one appears.

PORTNAME=	audiomuse-ai
DISTVERSIONPREFIX=	v
DISTVERSION=	3.7.1
CATEGORIES=	audio # machine-learning

MAINTAINER=	e4779@4779.ru
COMMENT=	Sonic analysis and smart playlists for Navidrome (native CPU sidecar)
WWW=		https://github.com/NeptuneHub/AudioMuse-AI

LICENSE=	AGPLv3
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		python:3.10+,run

USE_GITHUB=	yes
GH_ACCOUNT=	NeptuneHub
GH_PROJECT=	AudioMuse-AI

# service user/group are created on the host at deploy time (house pattern,
# see stash/_stash); the port ships no USERS= to avoid UIDs/GIDs coupling.

USE_RC_SUBR=	audiomuse audiomuse_worker
SUB_FILES=	audiomuse-setup-models

NO_ARCH=	yes
NO_BUILD=	yes

RUN_DEPENDS=	gunicorn:www/py-gunicorn \
		${PYTHON_SITELIBDIR}/flask/__init__.py:www/py-flask \
		${PYTHON_SITELIBDIR}/flask_cors/__init__.py:www/py-flask-cors \
		${PYTHON_SITELIBDIR}/requests/__init__.py:www/py-requests \
		${PYTHON_SITELIBDIR}/sklearn/__init__.py:science/py-scikit-learn \
		${PYTHON_SITELIBDIR}/yaml/__init__.py:devel/py-pyyaml \
		${PYTHON_SITELIBDIR}/six.py:devel/py-six \
		${PYTHON_SITELIBDIR}/rapidfuzz/__init__.py:devel/py-rapidfuzz \
		${PYTHON_SITELIBDIR}/psycopg2/__init__.py:databases/py-psycopg2 \
		${PYTHON_SITELIBDIR}/ftfy/__init__.py:textproc/py-ftfy \
		${PYTHON_SITELIBDIR}/flasgger/__init__.py:www/py-flasgger \
		${PYTHON_SITELIBDIR}/sqlglot/__init__.py:databases/py-sqlglot \
		${PYTHON_SITELIBDIR}/umap/__init__.py:math/py-umap-learn \
		${PYTHON_SITELIBDIR}/psutil/__init__.py:sysutils/py-psutil \
		${PYTHON_SITELIBDIR}/onnx/__init__.py:misc/py-onnx \
		${PYTHON_SITELIBDIR}/librosa/__init__.py:audio/py-librosa \
		${PYTHON_SITELIBDIR}/soxr/__init__.py:audio/py-soxr \
		${PYTHON_SITELIBDIR}/flatbuffers/__init__.py:devel/py-flatbuffers \
		${PYTHON_SITELIBDIR}/packaging/__init__.py:devel/py-packaging \
		${PYTHON_SITELIBDIR}/google/protobuf/__init__.py:devel/py-protobuf \
		${PYTHON_SITELIBDIR}/sympy/__init__.py:math/py-sympy \
		${PYTHON_SITELIBDIR}/httpx/__init__.py:www/py-httpx \
		${PYTHON_SITELIBDIR}/transformers/__init__.py:misc/py-transformers \
		${PYTHON_SITELIBDIR}/huggingface_hub/__init__.py:misc/py-huggingface-hub \
		${PYTHON_SITELIBDIR}/tokenizers/__init__.py:textproc/py-tokenizers \
		${PYTHON_SITELIBDIR}/jwt/__init__.py:www/py-pyjwt \
		${PYTHON_SITELIBDIR}/argon2/__init__.py:security/py-argon2-cffi \
		${PYTHON_SITELIBDIR}/cryptography/__init__.py:security/py-cryptography \
		${PYTHON_SITELIBDIR}/zstandard/__init__.py:archivers/py-zstandard \
		${PYTHON_SITELIBDIR}/onnxruntime/__init__.py:misc/py-onnxruntime \
		${PYTHON_SITELIBDIR}/numpy/__init__.py:math/py-numpy \
		${PYTHON_SITELIBDIR}/scipy/__init__.py:science/py-scipy \
		${PYTHON_SITELIBDIR}/numba/__init__.py:devel/py-numba \
		${PYTHON_SITELIBDIR}/soundfile.py:audio/py-SoundFile \
		${PYTHON_SITELIBDIR}/av/__init__.py:multimedia/py-av \
		${PYTHON_SITELIBDIR}/numkong/__init__.py:math/py-numkong \
		${PYTHON_SITELIBDIR}/langdetect/__init__.py:textproc/py-langdetect \
		${PYTHON_SITELIBDIR}/wn/__init__.py:textproc/py-wn \
		${PYTHON_SITELIBDIR}/google/genai/__init__.py:misc/py-google-genai

do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/share/audiomuse-ai
	cd ${WRKSRC} && ${FIND} . -type f \
		-not -path './test/*' -not -path './docs/*' -not -path './deployment/*' \
		-not -path './native-build/*' -not -path './example/*' -not -path './screenshot/*' \
		-not -path './.github/*' -not -path './requirements/*' -not -path './.git/*' \
		-not -path './scripts/standalone/*' \
		-not -name '*.yml' -not -name '*.toml' -not -name 'Dockerfile*' \
		-not -name .coveragerc -not -name .gitignore -not -name .gitattributes \
		-not -name .dockerignore -not -name .codespellrc -not -name .sonarcloud.properties \
		-not -name .trivyignore -not -name 'pytest.ini' -not -name 'LICENSE' \
		-not -name 'CODE_OF_CONDUCT.md' -not -name 'CONTRIBUTING.md' \
		-not -name 'SECURITY.md' -not -name 'README.md' -not -name '*.spec' \
		| while read -r f; do \
			${MKDIR} ${STAGEDIR}${PREFIX}/share/audiomuse-ai/$$(dirname $${f#./}); \
			${INSTALL_DATA} $${f} ${STAGEDIR}${PREFIX}/share/audiomuse-ai/$${f#./}; \
		done
	${MKDIR} ${STAGEDIR}${PREFIX}/share/audiomuse-ai/scripts/standalone
	${INSTALL_DATA} ${WRKSRC}/scripts/standalone/assemble_model.py \
		${STAGEDIR}${PREFIX}/share/audiomuse-ai/scripts/standalone/
	${INSTALL_DATA} ${WRKSRC}/LICENSE ${STAGEDIR}${PREFIX}/share/audiomuse-ai/
	${INSTALL_SCRIPT} ${WRKDIR}/audiomuse-setup-models ${STAGEDIR}${PREFIX}/bin/
	${INSTALL_DATA} ${FILESDIR}/audiomuse.env.sample ${STAGEDIR}${PREFIX}/etc/audiomuse.env.sample

.include <bsd.port.mk>
