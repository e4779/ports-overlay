# hlab overlay: C++ core of CTranslate2 — inference engine for
# argos-translate-lt / LibreTranslate (runbook 28). Upstream ships no PyPI
# sdist (wheels only); split lib/binding the sentencepiece way:
# this port = shared library, textproc/py-ctranslate2 = python binding.
# Submodule pins from git trees API at v4.8.5 (cpu_features/spdlog/thrust).
# OPENMP_RUNTIME defaults to INTEL upstream — override to COMP (base clang
# + llvm openmp), otherwise cmake demands libiomp5.
# NB: with FreeBSD OpenBLAS on Zen 5, consumers MUST run with
# OPENBLAS_CORETYPE=Haswell (broken Zen5 kernel -> SIGSEGV on big GEMM;
# handled in www/libretranslate rc.d). Retire if an official port appears.

PORTNAME=	ctranslate2
DISTVERSIONPREFIX=	v
DISTVERSION=	4.8.5
PORTREVISION=	1
CATEGORIES=	textproc

MAINTAINER=	e4779@4779.ru
COMMENT=	Fast inference engine for Transformer models (C++ library)
WWW=		https://github.com/OpenNMT/CTranslate2

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

LIB_DEPENDS=	libopenblas.so:math/openblas

USES=		cmake
USE_GITHUB=	yes
GH_ACCOUNT=	OpenNMT
GH_PROJECT=	CTranslate2
GH_TUPLE=	gabime:spdlog:76fb40d95455f249bd70824ecfcae7a8f0930fa3:spdlog/third_party/spdlog \
		google:cpu_features:8a494eb1e158ec2050e5f699a504fbc9b896a43b:cpu_features/third_party/cpu_features \
		NVIDIA:cccl:b5fe509fd11a925f90d6495176707cc1184eed9d:thrust/third_party/thrust

# ENABLE_CPU_DISPATCH off: google/cpu_features does not recognize the CPU
# vendor on FreeBSD ("Unknown CPU vendor" warning) -> runtime ISA dispatch
# is untrusted here; generic x86-64 build.
CMAKE_ON=	WITH_OPENBLAS
CMAKE_OFF=	WITH_MKL WITH_RUY WITH_DNNL BUILD_TESTS BUILD_CLI ENABLE_CPU_DISPATCH
CMAKE_ARGS+=	-DOPENMP_RUNTIME:STRING=COMP

.include <bsd.port.mk>
