# ports-overlay — собственные порты hlab

Poudriere-оверлей домашнего сервера hlab (FreeBSD 15.1): собственные
порты и патчи, из которых фабрика собирает пакеты в подписанный
репозиторий `hlab`.

```
net/microsocks    SOCKS-прокси с патчем v4-only (upstream слушает v6)
www/copyparty     файлопомойка, версии свежее дерева портов
multimedia/stash  медиа-органайзер; официальный freebsd-бинарь из релиза
editors/mg        мини-эмакс: форк troglobit v4.2 (UTF-8, подсветка, C-h q)
```

Использование (на хосте):

```sh
doas poudriere bulk -j 151amd64 -p default net/microsocks   # сборка
pkg update && pkg install microsocks                        # установка
```

Runbook: `docs/freebsd/05-pkg-factory.md` в репо
[e4779/homelab](https://github.com/e4779/homelab) (или gitverse-зеркало).

## Лицензия

Файлы упаковки и патчи — ISC (см. [LICENSE](LICENSE)). Портируемое
программное обеспечение распространяется по собственным лицензиям
upstream (microsocks — MIT, copyparty — Apache-2.0) и НЕ входит в охват
этой лицензии; условия каждого порта — в его `Makefile` (`LICENSE=`).
