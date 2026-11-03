PORTNAME=	bhyve-uartfix
PORTVERSION=	15.1
PORTEPOCH=	1
PORTREVISION=	3
CATEGORIES=	sysutils
MASTER_SITES=	#
DISTFILES=	#

MAINTAINER=	e@4779.name
COMMENT=	bhyve from base sys with the UART console EOF spin fix (PR 300475)
WWW=		https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=300475

LICENSE=	BSD2CLAUSE

PLIST_FILES=	libexec/bhyve-uartfix

# No distfile: sources come from the build jail's own /usr/src
# (method=url releases carry it; mounted read-only during bulk).
# A minimal src-tree skeleton is assembled under WRKDIR so the
# out-of-tree build with the src tree's mk files (-m) resolves
# SRCTOP-relative paths; files/patch-uart_backend applies the fix.

WRKSRC=		${WRKDIR}/src/usr.sbin/bhyve
NO_WRKSUBDIR=	yes

SRC=		/usr/src
DEST=		${WRKDIR}/src


do-extract:
	${MKDIR} ${DEST}/usr.sbin ${DEST}/lib ${DEST}/contrib \
		${DEST}/sys/conf ${DEST}/sys/sys ${DEST}/sys/libkern \
		${DEST}/sys/cam ${DEST}/sys/contrib 		${DEST}/sys/x86 ${DEST}/sys/dev ${DEST}/sys/net ${DEST}/sys/netgraph ${DEST}/sys/contrib/dev \
		${DEST}/sys/contrib/libfdt \
		${DEST}/sys/amd64 \
		${DEST}/lib/lib9p/backend ${DEST}/lib/lib9p/sbuf \
		${DEST}/lib/lib9p/transport
	cd ${SRC}/usr.sbin/bhyve && ${CP} -R . ${WRKSRC}/
	cd ${SRC}/lib/lib9p && ${CP} -R . ${DEST}/lib/lib9p/
	cd ${SRC}/contrib/lib9p && ${CP} -R . ${DEST}/contrib/lib9p/
	cd ${SRC}/sys/conf && ${CP} -R . ${DEST}/sys/conf/
	cd ${SRC}/sys/sys && ${CP} -R . ${DEST}/sys/sys/
	cd ${SRC}/sys/libkern && ${CP} -R . ${DEST}/sys/libkern/
	cd ${SRC}/sys/cam && ${CP} -R . ${DEST}/sys/cam/
	cd ${SRC}/sys/contrib/libfdt && ${CP} -R . ${DEST}/sys/contrib/libfdt/
	cd ${SRC}/sys/contrib/dev/acpica && ${CP} -R . ${DEST}/sys/contrib/dev/acpica/
	cd ${SRC}/sys/x86 && ${CP} -R . ${DEST}/sys/x86/
	cd ${SRC}/sys/dev && ${CP} -R . ${DEST}/sys/dev/
	cd ${SRC}/sys/net && ${CP} -R . ${DEST}/sys/net/
	cd ${SRC}/sys/netgraph && ${CP} -R . ${DEST}/sys/netgraph/
	cd ${SRC}/sys/amd64/vmm && ${CP} -R . ${DEST}/sys/amd64/vmm/


do-build:
	cd ${WRKSRC} && grep -q uart_read_hup uart_backend.c || \
		${PATCH} -p0 < ${FILESDIR}/uart_backend.patch
	${MAKE_CMD} -m ${SRC}/share/mk -C ${DEST}/lib/lib9p \
		SRCTOP=${DEST} -DNO_OBJ -DNO_WERROR all
	${MAKE_CMD} -m ${SRC}/share/mk -C ${WRKSRC} SRCTOP=${DEST} \
		-DNO_OBJ -DNO_WERROR LDFLAGS+=-L${DEST}/lib/lib9p all

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/bhyve ${STAGEDIR}${PREFIX}/libexec/bhyve-uartfix

.include <bsd.port.mk>
