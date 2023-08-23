#!/usr/bin/env sh

DFU_UTIL="dfu-util"
/data/openpilot/selfdrive/ui/qt/spinner &
python -c "from panda import Panda; Panda().reset(enter_bootstub=True); Panda().reset(enter_bootloader=True)" || true
sleep 1
$DFU_UTIL -d 0483:df11 -a 0 -s 0x08004000 -D /data/openpilot/panda/board/obj/panda.bin.signed
$DFU_UTIL -d 0483:df11 -a 0 -s 0x08000000:leave -D /data/openpilot/panda/board/obj/bootstub.panda.bin
sleep 1
killall spinner &
reboot
