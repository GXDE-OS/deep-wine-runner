#!/bin/bash
SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
# /opt 目录识别
option=""

if [[ -d /usr/lib32 ]] && [[ -d $SHELL_FOLDER/lib32 ]]; then
    option="$option --dev-bind $SHELL_FOLDER/lib32 /usr/lib32 "
fi

if [[ -d /usr/lib64 ]] && [[ -d $SHELL_FOLDER/lib64 ]]; then
    option="$option --dev-bind $SHELL_FOLDER/lib64 /usr/lib64 "
fi

if [[ -d /usr/share/fonts ]]; then
    option="$option --dev-bind /usr/share/fonts /usr/share/fonts "
fi

if [[ -d $SHELL_FOLDER/gnemul ]]; then
    if [[ ! -d /usr/gnemul ]]; then
        pkexec mkdir -p /usr/gnemul
    fi
    option="$option --dev-bind $SHELL_FOLDER/gnemul /usr/gnemul "
fi

"$SHELL_FOLDER/bwrap" --dev-bind / / \
    --dev-bind "$SHELL_FOLDER/bin" /usr/bin \
    --dev-bind "$SHELL_FOLDER/bin" /bin \
    --dev-bind "$SHELL_FOLDER/lib" /usr/lib \
    --dev-bind "$SHELL_FOLDER/lib" /lib \
    --dev-bind /usr/lib/locale /usr/lib/locale \
    --dev-bind "$SHELL_FOLDER/share" /usr/share \
    $option \
    $SHELL_FOLDER/runner/deepin-wine-runner $*
