# SPDX-License-Identifier: GPL-2.0-or-later
"""Launcher translations. The Russian text is the key; other languages are looked up by it.

ui_language in the launcher settings: one of LANGUAGES or "" (the system locale; English when
the launcher has no translation for it).
"""
import os

EN = {
    "Папка DLC": "DLC folder",
    "Выбрать папку DLC": "Choose the DLC folder",
    "Не использовать DLC": "Don't use DLC",
    "Найдено DLC: {}": "DLC found: {}",
    "Не используется": "Not used",
    "Нет DLC этой игры в папке": "No DLC of this game in the folder",
    # Window, pages, buttons
    "Запустить": "Play",
    "Остановить": "Stop",
    "Настройки": "Settings",
    "Журнал": "Log",
    "Не удалось запустить: {}": "Could not start: {}",
    "Копировать": "Copy",
    "Экспорт журнала…": "Export log…",
    "Экспорт журнала": "Export log",
    "Журнал скопирован": "Log copied",
    "Журнал сохранён: {}": "Log saved: {}",
    "Не удалось сохранить журнал: {}": "Could not save the log: {}",
    "\n— игра завершилась (код {}) —\n": "\n— the game exited (code {}) —\n",
    # Launcher language
    "Язык лаунчера": "Launcher language",
    "Как в системе": "System",
    "Применится после перезапуска лаунчера, пока игра запущена":
        "Applies after restarting the launcher while the game is running",
    # Game
    "Игра": "Game",
    "Папка игры ({})": "Game folder ({})",
    "Папка игры": "Game folder",
    "Выбрать папку с eboot.bin": "Choose the folder with eboot.bin",
    "Открыть в файловом менеджере": "Open in the file manager",
    "Папка сохранений": "Saves folder",
    "Выбрать папку сохранений": "Choose the saves folder",
    "Вернуть папку по умолчанию": "Back to the default folder",
    "Язык системы": "System language",
    "По умолчанию: {}": "Default: {}",
    "Найдены сохранения": "Saves found",
    "Сохранений пока нет: игра создаст их здесь": "No saves yet: the game will create them here",
    "не выбрана": "not chosen",
    "Нет eboot.bin в папке": "No eboot.bin in the folder",
    "Управление": "Controls",
    "Геймпад": "Gamepad",
    "Назначение кнопок; применяется при запуске игры": "Button assignments; applied when the game starts",
    "Назначить": "Assign",
    "Сбросить": "Reset",
    "{} (по умолчанию)": "{} (default)",
    "не назначено": "not assigned",
    "Нажмите клавишу или кнопку… (Esc — отмена)": "Press a key or a button… (Esc cancels)",
    "Крест": "Cross",
    "Круг": "Circle",
    "Квадрат": "Square",
    "Треугольник": "Triangle",
    "Крестовина вверх": "D-pad up",
    "Крестовина вниз": "D-pad down",
    "Крестовина влево": "D-pad left",
    "Крестовина вправо": "D-pad right",
    "Движение вперёд": "Move forward",
    "Движение назад": "Move back",
    "Движение влево": "Move left",
    "Движение вправо": "Move right",
    "Камера вверх": "Camera up",
    "Камера вниз": "Camera down",
    "Камера влево": "Camera left",
    "Камера вправо": "Camera right",
    "Контроллер": "Controller",
    "Выбранный берётся, как только подключится": "The chosen one is used as soon as it connects",
    "Первый подключённый": "First connected",
    "{} (не подключён)": "{} (not connected)",
    "Монитор": "Monitor",
    "Основной": "Primary",
    ", основной": ", primary",
    "eboot.bin не читается как расшифрованный исполняемый файл PS4: сделайте дамп заново":
        "eboot.bin cannot be read as a decrypted PS4 executable: dump the game again",
    "Папка игры (с eboot.bin)": "Game folder (with eboot.bin)",
    # Languages
    "Английский": "English",
    "Русский": "Russian",
    "Французский": "French",
    "Испанский": "Spanish",
    # Mods
    "Обновить список": "Refresh the list",
    # Patches
    "Сторонние патчи": "Third-party patches",
    "Папка патчей": "Patches folder",
    "Выбрать папку патчей": "Choose the patches folder",
    "Открыть папку патчей": "Open the patches folder",
    "Патчей нет": "No patches",
    "Автор: {}": "Author: {}",
    # Screen
    "Экран": "Display",
    "Разрешение вывода": "Output resolution",
    "Апскейлер дорисовывает кадр; Steam Deck — 720p": "The upscaler fills the frame; Steam Deck: 720p",
    "Полноэкранный режим": "Fullscreen",
    "Смена разрешения на лету": "Live resolution changes",
    "Без перезапуска, но медленнее на Steam Deck и старых GPU":
        "No restart needed, but slower on the Steam Deck and older GPUs",
    "Авто (по видеокарте)": "Auto (by GPU)",
    "Выключена (быстрее)": "Off (faster)",
    "Включена": "On",
    "Режим показа кадров": "Present mode",
    "Разрешить HDR": "Allow HDR",
    # Upscaler
    "Апскейлер": "Upscaler",
    "Хранится в bbport.ini; в игре меняется через меню (Insert или L3+R3)":
        "Stored in bbport.ini; in game, change it in the menu (Insert or L3+R3)",
    "TAA (нативное сглаживание)": "TAA (native anti-aliasing)",
    "Выключен": "Off",
    "Пресет": "Preset",
    "Резкость (RCAS)": "Sharpening (RCAS)",
    "Сила резкости": "Sharpness",
    "Векторы движения объектов": "Object motion vectors",
    "Меньше гостинга на персонажах; стоит около 10% FPS": "Less ghosting on characters; costs about 10% FPS",
    "Показывать FPS": "Show FPS",
    "Ассеты найдены": "Assets found",
    "Нет ассетов: tools/fetch_fsr4_assets.sh": "No assets: tools/fetch_fsr4_assets.sh",
    "Ассеты для выбранного режима найдены": "Assets for the selected mode found",
    "{}. Соберите FSR 4.1.1 из своей DLL кнопкой «Выбрать DLL…» ниже":
        "{}. Build FSR 4.1.1 from your own DLL with the “Choose DLL…” button below",
    "FSR 4.1.1 из своей DLL AMD": "FSR 4.1.1 from your own AMD DLL",
    "Отменить": "Cancel",
    "Выбрать DLL…": "Choose DLL…",
    "DLL апскейлера AMD (amd_fidelityfx_upscaler_dx12.dll)": "AMD upscaler DLL (amd_fidelityfx_upscaler_dx12.dll)",
    "нет": "none",
    "Эта DLL не подходит": "This DLL does not fit",
    "{}: версия {}, модели FSR 4: {}.\n\nbbport повторяет только официальную FSR 4.1.x от AMD (модель v07_fp8_no_scale): например, FSR4_LATEST из OptiScaler или amd_fidelityfx_upscaler_dx12.dll из игры с FSR 4.1. Сборки сообщества (4.0.2b и подобные) устроены иначе и пока не поддерживаются.":
        "{}: version {}, FSR 4 models: {}.\n\nbbport replays AMD's official FSR 4.1.x only (model v07_fp8_no_scale): for example FSR4_LATEST from OptiScaler, or amd_fidelityfx_upscaler_dx12.dll from a game with FSR 4.1. Community builds (4.0.2b and the like) are laid out differently and are not supported yet.",
    "Загрузчик не подходит": "The loader does not fit",
    "Загрузчик FidelityFX (amd_fidelityfx_loader_dx12.dll или amd_fidelityfx_dx12.dll)":
        "FidelityFX loader (amd_fidelityfx_loader_dx12.dll or amd_fidelityfx_dx12.dll)",
    "\n— сборка FSR 4.1.1 из {} —\n": "\n— building FSR 4.1.1 from {} —\n",
    "Подготовка…": "Preparing…",
    "Запись проходов DLL под Proton: {} из {}": "Recording the DLL's passes under Proton: {} of {}",
    "Перевод проходов в SPIR-V…": "Translating the passes to SPIR-V…",
    "— сборка FSR 4.1.1 завершилась (код {}) —\n": "— FSR 4.1.1 build finished (code {}) —\n",
    "FSR 4.1.1 собран и выбран": "FSR 4.1.1 built and selected",
    "Сборка FSR 4.1.1 отменена": "FSR 4.1.1 build cancelled",
    "FSR 4.1.1 не собран": "FSR 4.1.1 was not built",
    "DLL не подходит: подробности в журнале": "The DLL does not fit: details in the log",
    "Не хватает программ для сборки: список в журнале": "Tools for the build are missing: the list is in the log",
    "Записанные проходы не совпали с тем, что повторяет bbport (другая версия DLL или новая видеокарта?): подробности в журнале":
        "The recorded passes do not match what bbport replays (another DLL version, or a new GPU?): details in the log",
    "Не найден загрузчик FidelityFX 2.x": "No FidelityFX loader 2.x found",
    "Не найден подходящий Proton: установите GE-Proton 10 или новее (ProtonUp-Qt) или Proton Experimental / Proton-CachyOS в Steam. Если они есть — запустите в Steam любую игру с этим Proton, чтобы Steam поставил его рантайм":
        "No suitable Proton found: install GE-Proton 10 or newer (ProtonUp-Qt), or Proton Experimental / Proton-CachyOS in Steam. If you have them, start any game with that Proton in Steam so that Steam installs its runtime",
    "Ни один Proton не запустил FSR 4.1 из этой DLL. Либо они слишком старые (подходят GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), либо DLL не включает FSR 4.1 на этой видеокарте (Steam Deck?): тогда соберите на ПК с Radeon RX 7000/9000 и скопируйте папку fsr4_411. Подробности в журнале":
        "No Proton started this DLL's FSR 4.1. Either they are too old (GE-Proton 10+, Proton Experimental, Proton-CachyOS 11 work), or the DLL does not enable FSR 4.1 on this GPU (Steam Deck?): then build on a PC with a Radeon RX 7000/9000 and copy the fsr4_411 folder. Details in the log",
    "На NixOS запись идёт на самой системе (systemd --user) через umu-launcher из nix-shell, а здесь их не нашлось: установите umu-launcher или Nix. Подробности в журнале":
        "On NixOS the recording runs on the system itself (systemd --user) with umu-launcher from nix-shell, and neither was found: install umu-launcher or Nix. Details in the log",
    "{}: FSR {}. Это официальная FSR 4.0.x от AMD: она включается только на видеокартах RDNA4 (RX 9000), а под Proton на других видеокартах не запускается, поэтому записать её нельзя.\n\nНужна FSR 4.1.x: например, FSR4_LATEST из OptiScaler или DLL из игры с FSR 4.1.":
        "{}: FSR {}. This is AMD's official FSR 4.0.x: it is enabled on RDNA4 GPUs (RX 9000) only and does not start under Proton on other GPUs, so it cannot be recorded.\n\nFSR 4.1.x is needed: for example FSR4_LATEST from OptiScaler, or the DLL of a game with FSR 4.1.",
    "{}: в этой DLL нет FSR 4. Нужна amd_fidelityfx_upscaler_dx12.dll версии 4.1.x.":
        "{}: this DLL has no FSR 4 inside. amd_fidelityfx_upscaler_dx12.dll version 4.1.x is needed.",
    "Это не загрузчик":
        "This is not the loader",
    "{} — это DLL апскейлера. Загрузчик называется amd_fidelityfx_loader_dx12.dll (у OptiScaler — amd_fidelityfx_dx12.dll) и лежит в той же папке игры, что и DLL апскейлера.":
        "{} is the upscaler DLL. The loader is called amd_fidelityfx_loader_dx12.dll (amd_fidelityfx_dx12.dll in OptiScaler) and lies in the same game folder as the upscaler DLL.",
    "{}: версия {}. Нужен загрузчик FidelityFX 2.x — из той же игры, что и DLL апскейлера.":
        "{}: version {}. A FidelityFX loader 2.x is needed, from the same game as the upscaler DLL.",
    "Рядом с DLL нет загрузчика: выберите amd_fidelityfx_loader_dx12.dll из папки игры":
        "No loader next to the DLL: choose amd_fidelityfx_loader_dx12.dll from the game's folder",
    "Собрать FSR 4.1.1 из amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: папка FSR4_LATEST, или из игры с FSR 4.1). Нужен GE-Proton 10+, Proton Experimental или Proton-CachyOS; 2–5 минут (RDNA4: вдвое дольше, ещё и вариант FP8)":
        "Build FSR 4.1.1 from amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: the FSR4_LATEST folder, or from a game with FSR 4.1). Needs GE-Proton 10+, Proton Experimental or Proton-CachyOS; 2–5 minutes (RDNA4: twice as long, with the FP8 variant)",
    "Сборка не удалась (код {}): подробности в журнале": "The build failed (code {}): details in the log",
    "Сглаживание в разрешении вывода без модели FSR": "Anti-aliasing at the output resolution, no FSR model",
    "DLSS найден (нужна видеокарта NVIDIA RTX)": "DLSS found (needs an NVIDIA RTX GPU)",
    # Online page
    "Эта сборка без модуля онлайна (libbbnet.so): игра только офлайн": "This build has no online module (libbbnet.so): offline play only",
    'Выключено: игра остаётся офлайн, как раньше': 'Off: the game stays offline, as before',
    'Играть онлайн': 'Play online',
    'Онлайн': 'Online',
    'Отмена': 'Cancel',
    'Пароль': 'Password',
    'Проверить': 'Test',
    'Проверить соединение': 'Test the connection',
    'Проверка…': 'Checking…',
    'Сервер shadNet': 'shadNet server',
    'Соединение': 'Connection',
    'Учётная запись': 'Account',
    'доступен': 'reachable',
    'недоступен': 'not reachable',
    "DLSS: библиотека NVIDIA": "DLSS: NVIDIA's library",
    "Выбрать файл…": "Choose a file…",
    "Убрать выбранную": "Remove the chosen one",
    "Своя: {}": "Your own: {}",
    "Из сборки: {}": "From this build: {}",
    "Нет: выберите libnvidia-ngx-dlss.so.* из DLSS SDK NVIDIA ({})": "None: choose libnvidia-ngx-dlss.so.* from NVIDIA's DLSS SDK ({})",
    "Эта сборка без моста DLSS (libbbport_dlss.so): DLSS работать не будет": "This build has no DLSS bridge (libbbport_dlss.so): DLSS will not work",
    "Библиотека DLSS NVIDIA (libnvidia-ngx-dlss.so.*)": "NVIDIA's DLSS library (libnvidia-ngx-dlss.so.*)",
    "Нужна библиотека для Linux": "A Linux library is needed",
    "{} — библиотека DLSS для Windows; на Linux NVIDIA её не загружает. Нужна libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}":
        "{} is the Windows DLSS library; NVIDIA's Linux driver does not load it. libnvidia-ngx-dlss.so.<version> from NVIDIA's DLSS SDK is needed: {}",
    "Не удалось прочитать файл": "Could not read the file",
    "Это не библиотека DLSS": "This is not the DLSS library",
    "Нужен файл libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}": "libnvidia-ngx-dlss.so.<version> from NVIDIA's DLSS SDK is needed: {}",
    "Не удалось скопировать библиотеку": "Could not copy the library",
    "DLSS {}: готово": "DLSS {}: ready",
    "Клавиатура и мышь": "Keyboard and mouse",
    "Камера мышью": "Mouse look",
    "Щелчок в окне игры захватывает мышь, F1 — отпускает": "A click in the game window takes the mouse, F1 releases it",
    "Чувствительность мыши": "Mouse sensitivity",
    "Инвертировать мышь по вертикали": "Invert mouse Y axis",
    "DLSS не найден: выберите библиотеку NVIDIA ниже (и нужна сборка с мостом DLSS). Игра включит FSR 3.1":
        "DLSS not found: choose NVIDIA's library below (a build with the DLSS bridge is needed too). The game will use FSR 3.1",
    "Нет или повреждён файл {}": "Missing or damaged file {}",
    # Effects
    "Пропуск заставок при запуске": "Skip the intro videos",
    # Frame rate
    "Частота кадров": "Frame rate",
    "Режим": "Mode",
    "Какой патч частоты кадров применить к игре": "Which frame rate patch to apply to the game",
    "Без ограничения (патч)": "Unlocked (patch)",
    "60 (как на PS4)": "60 (as on PS4)",
    "Ограничение FPS": "FPS limit",
    "0 — без ограничения; укажите число, чтобы ограничить FPS":
        "0: no limit; set a number to cap the frame rate",
    # Performance
    "Производительность": "Performance",
    "Двухстадийный конвейер GPU": "Two-stage GPU pipeline",
    "Быстрее на 20–30%; при нестабильности выключите": "20–30% faster; turn off if unstable",
    "Авто": "Auto",
    "Включён при 8 и более потоках процессора": "On with 8 or more CPU threads",
    "Включён": "On",
    "Стабильнее, но медленнее": "More stable, but slower",
    "Чтение данных GPU процессором": "GPU data readbacks by the CPU",
    "По умолчанию": "Default",
    "Фоновая загрузка в видеопамять": "Background pre-upload into VRAM",
    "Меньше рывков при подгрузке зон": "Fewer hitches when areas stream in",
    "Обычная": "Normal",
    "Без лишней видеопамяти": "No extra VRAM",
    "Полная": "Full",
    "Около 3 ГБ видеопамяти сверху": "About 3 GB more VRAM",
    # Mode
    "Режим работы": "Mode",
    "Новая: видеокарта работает с памятью игры напрямую, как в игре для ПК, а команды графики переводятся, а не эмулируются. Старая — модель памяти 0.3 со всеми исправлениями. Если драйвер не проходит проверку при запуске — старая":
        "The new one: the GPU works with the game's memory directly, as in a PC game, and graphics commands are translated rather than emulated. The old one: the memory model of 0.3 with all the fixes. If the driver fails the startup check, the old one",
    "Модель памяти и трансляции": "Memory and translation model",
    "Авто: новая на AMD, старая на других": "Auto: new on AMD, old on others",
    "Новая": "New",
    "Старая (как в 0.3)": "Old (as in 0.3)",
    "Синхронизация как в 0.3": "Synchronisation as in 0.3",
    "Для поиска регрессий: старая модель памяти и ожидания копий как в релизе 0.3":
        "For finding regressions: the old memory model and copy waits as released in 0.3",
    "Выключена": "Off",
    "Выключены": "Off",
    # Developer
    "Для разработчика": "Developer",
    "Статистика кадров в журнале": "Frame statistics in the log",
    "Сохранять журнал и статистику в файл": "Save the log and statistics to a file",
    "Диагностика вылетов": "Crash diagnostics",
    "Проверяет кучу игры и записывает записи в её память; немного медленнее":
        "Checks the game's heap and logs writes into its memory; a little slower",
    "В папку logs в каталоге данных: для разбора рывков и вылетов":
        "Into the logs folder of the data directory: to look into stutters and crashes",
    "Профиль GPU в журнале": "GPU profile in the log",
    "Слои валидации Vulkan": "Vulkan validation layers",
    "Сильно замедляет": "Much slower",
    "Доп. переменные (ИМЯ=значение через пробел)": "Extra variables (NAME=value, space-separated)",
    # Add to Steam
    "Добавить в Steam": "Add to Steam",
    "Игра в библиотеке Steam запускается сразу, с настройками этого лаунчера": "From the Steam library the game starts straight away, with this launcher's settings",
    "Добавить": "Add",
    "Steam не найден (или в него ещё никто не входил)": "Steam was not found (or nobody has signed in to it yet)",
    "Закройте Steam и нажмите «Добавить» ещё раз": "Close Steam and press Add again",
    "Пока игра добавляется, Steam нужно закрыть; потом он запустится снова. Закрыть Steam?": "Steam has to close while the game is added; it starts again afterwards. Close Steam?",
    "Отмена": "Cancel",
    "Закрыть Steam": "Close Steam",
    "Steam не закрылся. Закройте его сами и попробуйте ещё раз": "Steam did not close. Close it yourself and try again",
    "Не удалось добавить игру в Steam: {}": "Could not add the game to Steam: {}",
    # Online page
    "Онлайн": "Online",
    "Играть онлайн": "Play online",
    "Выключено: игра остаётся офлайн, как раньше": "Off: the game stays offline, as before",
    "Учётная запись": "Account",
    "Пароль": "Password",
    "Соединение": "Connection",
    "Проверить соединение": "Test the connection",
    "Проверить": "Test",
    "Сервер shadNet": "shadNet server",
    "Проверка…": "Checking…",
    "доступен": "reachable",
    "недоступен": "not reachable",
    # Button prompts
    "Применяется при запуске игры": "Applies when the game starts",
    "Поменять местами A и B": "Swap A and B",
    "Для контроллеров в стиле Nintendo: подтверждение на A, отмена на B. Применяется при запуске игры": "For Nintendo-style controllers: confirm on A, back on B. Applies when the game starts",
    "Поменять стики местами": "Swap the sticks",
    "Инвертировать камеру геймпада по горизонтали": "Invert the controller camera horizontally",
    "Инвертировать камеру геймпада по вертикали": "Invert the controller camera vertically",
    "Импортировать сохранения…": "Import saves…",
    "Импорт сохранений": "Import saves",
    "Это копия с PS4 на флешке (sdimg_*): она зашифрована ключами консоли. Экспортируйте сохранение без шифрования на PS4 (Apollo Save Tool) или через Save Wizard": "This is a PS4 copy for a USB drive (sdimg_*): it is encrypted with the console's keys. Export the save unencrypted on the PS4 (Apollo Save Tool) or with Save Wizard",
    "Импортировать сохранения?": "Import the saves?",
    "Из {} (изменены {}). Текущие сохранения сначала копируются в {}": "From {} (changed {}). The current saves are copied to {} first",
    "Импортировать": "Import",
    "Не удалось импортировать сохранения": "Could not import the saves",
    "Сохранения импортированы": "Saves imported",
    # Add to Steam with Flathub's Steam
    'Steam из Flatpak запускает игры в своей песочнице, где нет ни папки игры, ни драйверов: ярлык должен запускать игру вне её (flatpak-spawn --host). Для этого Steam нужно право org.freedesktop.Flatpak, с которым он может запускать программы в вашей системе. Выдать его?':
        'Flatpak Steam runs games inside its sandbox, which has neither the game folder nor the drivers: the shortcut has to start the game outside it (flatpak-spawn --host). For that, Steam needs the org.freedesktop.Flatpak permission, which lets it start programs on your system. Grant it?',
    'Выдать право':
        'Grant permission',
    'Не удалось выдать право Steam: {}':
        'Could not grant Steam the permission: {}',
    "О программе":
        "About",
    "Сначала закройте игру":
        "Close the game first",
    "Основано на bbport от deadinside28":
        "Based on bbport by deadinside28",
    "Лицензия":
        "License",
    'GNU GPL v2 или новее · Файлы игры не входят.': 'GNU GPL v2 or later · No game files included.',
    # Online page: the server
    'Адрес сервера (host:port)':
        'Server address (host:port)',
    'Сервер shadNet':
        'shadNet server',
    # Trophies page
    'В дампе игры нет трофеев (sce_sys/trophy)':
        'The game dump has no trophies (sce_sys/trophy)',
    'Записываются, когда игра их открывает, и показываются в игре':
        'Recorded when the game unlocks them, and shown in the game',
    'Ключ трофеев':
        'Trophy key',
    'Неверный ключ трофеев: названия недоступны':
        'Wrong trophy key: the names are unavailable',
    'Получен {}':
        'Earned {}',
    'Получено {} из {}':
        '{} of {} earned',
    'Скрытый трофей':
        'Hidden trophy',
    'Трофеи':
        'Trophies',
    'Платиновый':
        'Platinum',
    'Золотой':
        'Gold',
    'Серебряный':
        'Silver',
    'Бронзовый':
        'Bronze',
    "Вход в shadNet": "shadNet sign-in",
    "неверное имя или пароль": "wrong name or password",
    "такой учётной записи нет на этом сервере": "no such account on this server",
    "эта учётная запись уже в сети (игра запущена?)": "this account is already signed in (is the game running?)",
    "вход выполнен": "signed in",
    "вход не удался ({})": "sign-in failed ({})",
    # About: Thanks
    'Благодарности': 'Thanks',
    'Без них ничего этого не было бы': 'None of this would be possible without them',
    'Порт и его код': 'The port and its code',
    'Помощь и тесты': 'Help and testing',
    'Другие благодарности': 'Also thanks to',
    'bbport — порт, на котором построен весь этот проект': 'bbport, the port this whole project is built on',
    'Игра по сети, DLSS, страница читов, добавление в Steam, значок, пропуск конвейеров, которые драйвер не может создать, и игра без вылета при нехватке видеопамяти': 'Online play, DLSS, the cheats page, Add to Steam, the icon, skipping pipelines the driver cannot create, and no crash when video memory runs out',
    'Собрал и адаптировал десятки исправлений: вылеты при загрузке, чёрные изображения, апскейлер, строка производительности в журнале': 'Gathered and adapted dozens of fixes: crashes while loading, black images, the upscaler, the performance line in the log',
    'Чёрный предпросмотр персонажа, картинка экрана загрузки и память кэша текстур': "The black character preview, the loading screen's picture and the texture cache's memory",
    'Кэш текстур вовремя освобождает видеопамять': 'The texture cache frees video memory in time',
    'Вылеты при загрузке областей': 'Crashes while loading areas',
    'Интерфейс, пропадавший не в 1080p, векторы движения больших чудовищ и ошибка памяти': 'The interface vanishing outside 1080p, motion vectors for the large beasts and a memory fault',
    'Вылеты при загрузке некоторых карт и меню жестов с клавиатуры': 'Crashes when loading some maps and the gestures menu from the keyboard',
    'Экранная клавиатура для имени персонажа и уведомление о компиляции шейдеров': "The on-screen keyboard for the character's name and the shader compiling notice",
    'Сетевые библиотеки игры по сети и сервер для своего кооператива': 'The online play libraries and the server for your own co-op',
    'Основа поддержки DLSS и модель FSR 4 без шлейфов за персонажами': 'The groundwork for DLSS, and the FSR 4 model without trails behind characters',
    'Апскейлер FSR 3.1': 'The FSR 3.1 upscaler',
    'Игра запускается, когда DLSS нельзя использовать': 'The game starts when DLSS cannot be used',
    'Перевод на упрощённый китайский': 'The Simplified Chinese translation',
    'Звук игры на полной громкости': "The game's audio at full level",
    'Флажки и ползунки внутриигрового меню': "The in-game menu's checkboxes and sliders",
    'Подробные отчёты с журналами и проверка исправлений': 'Detailed reports with logs, and testing the fixes',
    'Идея поменять местами A и B на контроллерах в стиле Nintendo': 'The idea of swapping A and B on Nintendo-style controllers',
    'Проверка исправления видеопамяти': 'Testing the video memory fix',
    'Рендерер и компилятор шейдеров': 'The renderer and shader recompiler',
    'Инструмент для сборки AppImage': 'The tool that builds the AppImage',
    'Нашёл ошибку, из-за которой игра не запускалась на некоторых видеокартах, и ускорение камеры на DualShock 4': 'Found the bug that kept the game from starting on some graphics cards, and the camera speeding up on a DualShock 4',
    'Нашёл, почему игра не запускалась в игровом режиме Steam Deck': "Found why the game did not start in the Steam Deck's Game Mode",
    'Нашёл, при каких эффектах зависают загрузки на NVIDIA': 'Found which effects freeze loading screens on NVIDIA',
    'ps4-pkg-extractor: установка игры из файлов .pkg': 'ps4-pkg-extractor: installing the game from .pkg files',
    # Shader cache
    'Кэш шейдеров': 'Shader cache',
    'Очистить': 'Clear',
    '{}. Если после обновления картинка выглядит странно, очистите его: шейдеры соберутся заново (первые минуты в каждой зоне возможны рывки)': '{}. If the picture looks wrong after an update, clear it: the shaders are built again (some stutter in each area for the first minutes)',
    'Пусто: шейдеры соберутся при игре': 'Empty: the shaders are built as you play',
    'Очистить кэш шейдеров?': 'Clear the shader cache?',
    'Игра соберёт шейдеры заново: первые минуты в каждой зоне возможны рывки. Сохранения и настройки не затрагиваются.': 'The game builds the shaders again: some stutter in each area for the first minutes. Saves and settings are not touched.',
    'Названия трофеев на английском без ключа и звук при получении трофея': 'Trophy names in English without the key, and the sound when one is earned',
    'Буфер трафарета, в который писали цветные изображения': 'The stencil buffer that colour images were writing into',
    'Вход на публичный сервер shadNet без отключения': 'Staying signed in on the public shadNet server',
    'Установить из PKG': 'Install from PKG',
    'Выбрать .pkg…': 'Choose .pkg…',
    'Файлы .pkg: игра, обновление, DLC': '.pkg files: game, update, DLC',
    'Куда установить игру': 'Where to install the game',
    'Установка…': 'Installing…',
    'Игра установлена: {}': 'Game installed: {}',
    'Не удалось установить: подробности в журнале': 'Could not install: details in the log',
    'Выход из игры из меню с контроллера, меню в пределах экрана и половины тачпада на Xbox': 'Quitting from the menu with a controller, the menu kept within the screen, and the touchpad halves on Xbox pads',
    'Вылет видеоплеера при его остановке': 'A video player crash when it stops',
    'Язык внутриигрового меню при запуске без окна лаунчера': "The in-game menu's language when starting without the launcher window",
    'DLSS в AppImage на NVIDIA': 'DLSS in the AppImage on NVIDIA',
    'Сверхширокие мониторы без растянутой картинки': 'Ultrawide monitors without a stretched picture',
    'Движение с клавиатуры: круглая диагональ и последняя нажатая клавиша': 'Keyboard movement: a round diagonal and the last key pressed',
    'Отладка вылетов: процесс ждёт отладчик (BB_FAULT_WAIT)': 'Crash debugging: the process waits for a debugger (BB_FAULT_WAIT)',
    'Видеопамять на картах с 4 ГБ и вылеты: флипы, swapchain, дескрипторы и ошибки страниц; смена стиков и инверсия камеры, импорт сохранений, выбор версии': 'Video memory on 4 GB cards and crashes: flips, the swapchain, descriptors and page faults; swapped sticks and camera inversion, save import, the version selector',
    'Большие группы команд записи и swapchain после изменений экрана': 'Large recorded command groups and the swapchain after display changes',
    # GODZILLA (gzport)
    'GODZILLA {}, версия 1.01':
        'GODZILLA {}, version 1.01',
    'GODZILLA добавлена в библиотеку Steam':
        'GODZILLA added to the Steam library',
    'GODZILLA — товарный знак Toho Co., Ltd.; игра для PS4 издана Bandai Namco Entertainment. Этот проект с ними не связан.':
        'GODZILLA is a trademark of Toho Co., Ltd.; the PS4 game was published by Bandai Namco Entertainment. This project is not affiliated with them.',
    'XML-патчи в формате shadPS4 для версии 01.01 из папки патчей. Применяются при запуске.':
        'shadPS4-format XML patches for version 01.01 from the patches folder. Applied at start.',
    'eboot.bin не от версии 1.01: скопируйте eboot.bin из дампа обновления 1.01 в папку игры с заменой':
        'eboot.bin is not from 1.01: copy eboot.bin from the dumped 1.01 update into the game folder, replacing it',
    'gzport — нативный порт для Linux':
        'gzport — native Linux port',
    'Авторы bbport и bloodborne_linux, на которых построен gzport, и все, кто им помогал':
        'The authors of bbport and bloodborne_linux, which gzport is built on, and everyone who helped them',
    'В папке игры нет: {}. Распакуйте игру и обновление 1.01 заново':
        'Missing from the game folder: {}. Extract the game and the 1.01 update again',
    'В этой папке нет сохранений GODZILLA (SAVEDATA00 с DATA.BIN)':
        'No GODZILLA saves in this folder (SAVEDATA00 with DATA.BIN)',
    'Игра идёт с 60 FPS, как на PS4. Выше 60 FPS: нужен патч частоты кадров, его пока нет':
        'The game runs at 60 FPS, as on the PS4. Above 60 FPS needs a frame-rate patch, not available yet',
    'Для GODZILLA пока недоступен: игра рисует кадр прямо в разрешении вывода':
        'Not available for GODZILLA yet: the game renders its frame at the output resolution itself',
    'Игра, обновление 1.01 и DLC из ваших файлов .pkg':
        'The game, update 1.01 and DLC from your .pkg files',
    'Ключ трофеев PS4 (TrophyKey в shadPS4), 32 шестнадцатеричных символа: с ним названия и описания на языке игры. Хранится на этом компьютере. Без него видны только значки':
        "The PS4's trophy key (TrophyKey in shadPS4), 32 hexadecimal digits: with it, the names and descriptions are in the game's language. Kept on this computer. Without it, only the icons are shown",
    'Нативный порт для Linux, версия {}':
        'Native Linux port, version {}',
    'Нужен патч для версии 1.01, его пока нет':
        'Needs a patch for version 1.01, not available yet',
    'Нужно обновление 1.01: скопируйте файлы дампа обновления 1.01 в папку игры с заменой (найдена версия {})':
        'The 1.01 update is needed: copy the dumped 1.01 update into the game folder, replacing files (found version {})',
    'Основано на bloodborne_linux от ayozetr':
        'Based on bloodborne_linux by ayozetr',
    'bloodborne_linux: порт для Linux, на котором построен gzport':
        'bloodborne_linux: the Linux port gzport is built on',
    'Папка с сохранениями GODZILLA':
        'Folder with GODZILLA saves',
    'Патчи игры':
        'Game patches',
    'Португальский (Бразилия)':
        'Portuguese (Brazil)',
    'Это не GODZILLA (найдено {}): нужна GODZILLA (CUSA02046) с обновлением 1.01':
        'This is not GODZILLA (found {}): GODZILLA (CUSA02046) with update 1.01 is needed',
    'Тачпад, левая половина':
        'Touchpad, left half',
    'Тачпад, правая половина':
        'Touchpad, right half',
    'Настройки по умолчанию':
        'Defaults',
    'Восстановить мои настройки по умолчанию':
        'Restore my defaults',
    'Вернуть':
        'Restore',
    'Сохранить текущие как мои настройки по умолчанию':
        'Save current as my defaults',
    'Настройки лаунчера и bbport.ini, без назначений кнопок':
        "The launcher's and bbport.ini's settings, without button bindings",
    'Сохранить':
        'Save',
    'Из {}':
        'From {}',
    'Своих настроек по умолчанию пока нет: восстанавливаются встроенные (папки и ключ трофеев не меняются)':
        'No defaults of your own yet: the built-in ones are restored (folders and the trophy key stay)',
    'Не удалось прочитать {}':
        'Could not read {}',
    'Восстановить настройки по умолчанию?':
        'Restore the defaults?',
    'Настройки лаунчера и bbport.ini станут такими, как в {}. Остальные строки bbport.ini, в том числе назначения кнопок, не меняются':
        "The launcher's and bbport.ini's settings become those in {}. The other lines of bbport.ini, button bindings included, stay as they are",
    'Своих настроек по умолчанию нет: настройки лаунчера и bbport.ini станут встроенными. Папки, ключ трофеев и назначения кнопок не меняются':
        "No defaults of your own: the launcher's and bbport.ini's settings become the built-in ones. Folders, the trophy key and button bindings stay as they are",
    'Настройки по умолчанию восстановлены':
        'Defaults restored',
    'Сохранить текущие настройки как свои по умолчанию?':
        'Save the current settings as your defaults?',
    'Они запишутся в {} вместо прежних, и «Вернуть» будет восстанавливать их':
        'They are written to {}, replacing the previous ones, and “Restore” brings them back',
    'Не удалось сохранить {}':
        'Could not save {}',
    'Текущие настройки сохранены как ваши по умолчанию':
        'Current settings saved as your defaults',
    # Online page (LAN versus)
    "Версус по локальной сети: VS MODE в меню «Онлайн» игры, через ваш сервер shadNet (shadnet-p2p с патчем gzport). У каждого игрока своя учётная запись на этом сервере": "Versus over the local network: VS MODE in the game's Online menu, through your own shadNet server (shadnet-p2p with the gzport patch). Every player has an account of their own on that server",
    "Как настроить версус по сети": "How to set up versus over the network",
    "Имя учётной записи на сервере shadNet (оно же ваше имя в игре) и её пароль. Пароль хранится на этом компьютере вместе с настройками лаунчера": "Your account name on the shadNet server (also your name in the game) and its password. The password is saved on this computer with the launcher settings",
    "Порт P2P (UDP)": "P2P port (UDP)",
    "Через него игроки соединяются напрямую; он должен быть открыт между компьютерами": "Players connect to each other directly through it; it must be open between the computers",
    "Укажите адрес сервера": "Enter the server address",
    "UDP сервера shadNet": "shadNet server UDP",
    "отвечает; сервер видит этот компьютер как {}": "answers; the server sees this computer as {}",
    "не отвечает: матч не соединится": "no answer: the match will not connect",
}

PT_BR = {
    "Папка DLC": "Pasta de DLC",
    "Выбрать папку DLC": "Escolher a pasta de DLC",
    "Не использовать DLC": "Não usar DLC",
    "Найдено DLC: {}": "DLC encontradas: {}",
    "Не используется": "Não usada",
    "Нет DLC этой игры в папке": "Nenhuma DLC deste jogo na pasta",
    # Window, pages, buttons
    "Запустить": "Jogar",
    "Остановить": "Parar",
    "Настройки": "Configurações",
    "Журнал": "Log",
    "Не удалось запустить: {}": "Não foi possível iniciar: {}",
    "Копировать": "Copiar",
    "Экспорт журнала…": "Exportar log…",
    "Экспорт журнала": "Exportar log",
    "Журнал скопирован": "Log copiado",
    "Журнал сохранён: {}": "Log salvo: {}",
    "Не удалось сохранить журнал: {}": "Não foi possível salvar o log: {}",
    "\n— игра завершилась (код {}) —\n": "\n— o jogo foi encerrado (código {}) —\n",
    # Launcher language
    "Язык лаунчера": "Idioma do launcher",
    "Как в системе": "Sistema",
    "Применится после перезапуска лаунчера, пока игра запущена":
        "Será aplicado após reiniciar o launcher enquanto o jogo estiver em execução",
    # Game
    "Игра": "Jogo",
    "Папка игры ({})": "Pasta do jogo ({})",
    "Папка игры": "Pasta do jogo",
    "Выбрать папку с eboot.bin": "Selecionar a pasta com eboot.bin",
    "Открыть в файловом менеджере": "Abrir no gerenciador de arquivos",
    "Папка сохранений": "Pasta de salvamentos",
    "Выбрать папку сохранений": "Selecionar a pasta de salvamentos",
    "Вернуть папку по умолчанию": "Restaurar a pasta padrão",
    "Язык системы": "Idioma do sistema",
    "По умолчанию: {}": "Padrão: {}",
    "Найдены сохранения": "Salvamentos encontrados",
    "Сохранений пока нет: игра создаст их здесь": "Ainda não há salvamentos: o jogo os criará aqui",
    "не выбрана": "não selecionada",
    "Нет eboot.bin в папке": "Não há eboot.bin na pasta",
    "Папка игры (с eboot.bin)": "Pasta do jogo (com eboot.bin)",
    # Languages
    "Английский": "Inglês",
    "Русский": "Russo",
    "Французский": "Francês",
    "Испанский": "Espanhol",
    "English": "Inglês",
    # Mods
    "Обновить список": "Atualizar a lista",
    # Patches
    "Сторонние патчи": "Patches de terceiros",
    "Папка патчей": "Pasta de patches",
    "Выбрать папку патчей": "Selecionar a pasta de patches",
    "Открыть папку патчей": "Abrir a pasta de patches",
    "Патчей нет": "Nenhum patch",
    "Автор: {}": "Autor: {}",
    # Screen
    "Экран": "Tela",
    "Разрешение вывода": "Resolução de saída",
    "Апскейлер дорисовывает кадр; Steam Deck — 720p": "O upscaler preenche o quadro; Steam Deck: 720p",
    "Полноэкранный режим": "Tela cheia",
    "Смена разрешения на лету": "Alteração de resolução em tempo real",
    "Без перезапуска, но медленнее на Steam Deck и старых GPU":
        "Não exige reinicialização, mas é mais lento no Steam Deck e em GPUs mais antigas",
    "Авто (по видеокарте)": "Automático (pela GPU)",
    "Выключена (быстрее)": "Desativado (mais rápido)",
    "Включена": "Ativado",
    "Режим показа кадров": "Modo de apresentação",
    "Разрешить HDR": "Permitir HDR",
    # Upscaler
    "Апскейлер": "Upscaler",
    "Хранится в bbport.ini; в игре меняется через меню (Insert или L3+R3)":
        "Armazenado em bbport.ini; no jogo, altere pelo menu (Insert ou L3+R3)",
    "TAA (нативное сглаживание)": "TAA (antisserrilhamento nativo)",
    "Выключен": "Desativado",
    "Пресет": "Predefinição",
    "Резкость (RCAS)": "Nitidez (RCAS)",
    "Сила резкости": "Intensidade da nitidez",
    "Векторы движения объектов": "Vetores de movimento dos objetos",
    "Меньше гостинга на персонажах; стоит около 10% FPS": "Menos ghosting nos personagens; custa cerca de 10% de FPS",
    "Показывать FPS": "Mostrar FPS",
    "Ассеты найдены": "Recursos encontrados",
    "Нет ассетов: tools/fetch_fsr4_assets.sh": "Recursos ausentes: tools/fetch_fsr4_assets.sh",
    "Ассеты для выбранного режима найдены": "Recursos encontrados para o modo selecionado",
    "{}. Соберите FSR 4.1.1 из своей DLL кнопкой «Выбрать DLL…» ниже":
        "{}. Gere o FSR 4.1.1 a partir da sua própria DLL com o botão “Escolher DLL…” abaixo",
    "FSR 4.1.1 из своей DLL AMD": "FSR 4.1.1 da sua própria DLL da AMD",
    "Отменить": "Cancelar",
    "Выбрать DLL…": "Escolher DLL…",
    "DLL апскейлера AMD (amd_fidelityfx_upscaler_dx12.dll)": "DLL do upscaler da AMD (amd_fidelityfx_upscaler_dx12.dll)",
    "нет": "nenhum",
    "Эта DLL не подходит": "Esta DLL não serve",
    "{}: версия {}, модели FSR 4: {}.\n\nbbport повторяет только официальную FSR 4.1.x от AMD (модель v07_fp8_no_scale): например, FSR4_LATEST из OptiScaler или amd_fidelityfx_upscaler_dx12.dll из игры с FSR 4.1. Сборки сообщества (4.0.2b и подобные) устроены иначе и пока не поддерживаются.":
        "{}: versão {}, modelos do FSR 4: {}.\n\nO bbport reproduz apenas o FSR 4.1.x oficial da AMD (modelo v07_fp8_no_scale): por exemplo, o FSR4_LATEST do OptiScaler ou a amd_fidelityfx_upscaler_dx12.dll de um jogo com FSR 4.1. Builds da comunidade (4.0.2b e similares) têm outra estrutura e ainda não são suportados.",
    "Загрузчик не подходит": "O carregador não serve",
    "Загрузчик FidelityFX (amd_fidelityfx_loader_dx12.dll или amd_fidelityfx_dx12.dll)":
        "Carregador do FidelityFX (amd_fidelityfx_loader_dx12.dll ou amd_fidelityfx_dx12.dll)",
    "\n— сборка FSR 4.1.1 из {} —\n": "\n— gerando o FSR 4.1.1 a partir de {} —\n",
    "Подготовка…": "Preparando…",
    "Запись проходов DLL под Proton: {} из {}": "Gravando as passagens da DLL no Proton: {} de {}",
    "Перевод проходов в SPIR-V…": "Traduzindo as passagens para SPIR-V…",
    "— сборка FSR 4.1.1 завершилась (код {}) —\n": "— geração do FSR 4.1.1 concluída (código {}) —\n",
    "FSR 4.1.1 собран и выбран": "FSR 4.1.1 gerado e selecionado",
    "Сборка FSR 4.1.1 отменена": "Geração do FSR 4.1.1 cancelada",
    "FSR 4.1.1 не собран": "O FSR 4.1.1 não foi gerado",
    "DLL не подходит: подробности в журнале": "A DLL não serve: detalhes no log",
    "Не хватает программ для сборки: список в журнале": "Faltam programas para a geração: a lista está no log",
    "Записанные проходы не совпали с тем, что повторяет bbport (другая версия DLL или новая видеокарта?): подробности в журнале":
        "As passagens gravadas não batem com o que o bbport reproduz (outra versão da DLL ou GPU nova?): detalhes no log",
    "Не найден загрузчик FidelityFX 2.x": "Carregador do FidelityFX 2.x não encontrado",
    "Не найден подходящий Proton: установите GE-Proton 10 или новее (ProtonUp-Qt) или Proton Experimental / Proton-CachyOS в Steam. Если они есть — запустите в Steam любую игру с этим Proton, чтобы Steam поставил его рантайм":
        "Nenhum Proton adequado encontrado: instale o GE-Proton 10 ou mais novo (ProtonUp-Qt), ou o Proton Experimental / Proton-CachyOS na Steam. Se já os tiver, abra qualquer jogo com esse Proton na Steam para que a Steam instale o runtime dele",
    "Ни один Proton не запустил FSR 4.1 из этой DLL. Либо они слишком старые (подходят GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), либо DLL не включает FSR 4.1 на этой видеокарте (Steam Deck?): тогда соберите на ПК с Radeon RX 7000/9000 и скопируйте папку fsr4_411. Подробности в журнале":
        "Nenhum Proton iniciou o FSR 4.1 desta DLL. Ou eles são antigos demais (funcionam GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), ou a DLL não ativa o FSR 4.1 nesta GPU (Steam Deck?): nesse caso, gere em um PC com Radeon RX 7000/9000 e copie a pasta fsr4_411. Detalhes no log",
    "На NixOS запись идёт на самой системе (systemd --user) через umu-launcher из nix-shell, а здесь их не нашлось: установите umu-launcher или Nix. Подробности в журнале":
        "No NixOS a gravação roda no próprio sistema (systemd --user) com o umu-launcher do nix-shell, e eles não foram encontrados: instale o umu-launcher ou o Nix. Detalhes no log",
    "{}: FSR {}. Это официальная FSR 4.0.x от AMD: она включается только на видеокартах RDNA4 (RX 9000), а под Proton на других видеокартах не запускается, поэтому записать её нельзя.\n\nНужна FSR 4.1.x: например, FSR4_LATEST из OptiScaler или DLL из игры с FSR 4.1.":
        "{}: FSR {}. Este é o FSR 4.0.x oficial da AMD: ele só é ativado em GPUs RDNA4 (RX 9000) e não inicia no Proton em outras GPUs, então não pode ser gravado.\n\nÉ preciso o FSR 4.1.x: por exemplo, o FSR4_LATEST do OptiScaler ou a DLL de um jogo com FSR 4.1.",
    "{}: в этой DLL нет FSR 4. Нужна amd_fidelityfx_upscaler_dx12.dll версии 4.1.x.":
        "{}: esta DLL não contém o FSR 4. É preciso a amd_fidelityfx_upscaler_dx12.dll versão 4.1.x.",
    "Это не загрузчик":
        "Este não é o carregador",
    "{} — это DLL апскейлера. Загрузчик называется amd_fidelityfx_loader_dx12.dll (у OptiScaler — amd_fidelityfx_dx12.dll) и лежит в той же папке игры, что и DLL апскейлера.":
        "{} é a DLL do upscaler. O carregador se chama amd_fidelityfx_loader_dx12.dll (amd_fidelityfx_dx12.dll no OptiScaler) e fica na mesma pasta do jogo que a DLL do upscaler.",
    "{}: версия {}. Нужен загрузчик FidelityFX 2.x — из той же игры, что и DLL апскейлера.":
        "{}: versão {}. É preciso um carregador do FidelityFX 2.x, do mesmo jogo que a DLL do upscaler.",
    "Рядом с DLL нет загрузчика: выберите amd_fidelityfx_loader_dx12.dll из папки игры":
        "Não há carregador ao lado da DLL: escolha a amd_fidelityfx_loader_dx12.dll da pasta do jogo",
    "Собрать FSR 4.1.1 из amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: папка FSR4_LATEST, или из игры с FSR 4.1). Нужен GE-Proton 10+, Proton Experimental или Proton-CachyOS; 2–5 минут (RDNA4: вдвое дольше, ещё и вариант FP8)":
        "Gerar o FSR 4.1.1 a partir de amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: pasta FSR4_LATEST, ou de um jogo com FSR 4.1). Requer GE-Proton 10+, Proton Experimental ou Proton-CachyOS; 2–5 minutos (RDNA4: o dobro, também com a variante FP8)",
    "Сборка не удалась (код {}): подробности в журнале": "A geração falhou (código {}): detalhes no log",
    "Сглаживание в разрешении вывода без модели FSR": "Antisserrilhamento na resolução de saída, sem modelo FSR",
    "Нет или повреждён файл {}": "Arquivo {} ausente ou corrompido",
    # Presets that are English source strings in the launcher
    "Native AA": "AA nativo",
    "Quality (x1.5)": "Qualidade (x1.5)",
    "Balanced (x1.7)": "Balanceado (x1.7)",
    "Performance (x2)": "Desempenho (x2)",
    "Ultra Performance (x3)": "Desempenho extremo (x3)",
    # Effects
    "Пропуск заставок при запуске": "Pular vídeos de introdução",
    # Frame rate
    "Частота кадров": "Taxa de quadros",
    "Режим": "Modo",
    "Какой патч частоты кадров применить к игре": "Qual patch de taxa de quadros aplicar ao jogo",
    "Без ограничения (патч)": "Sem limite (patch)",
    "60 (как на PS4)": "60 (como no PS4)",
    "Ограничение FPS": "Limite de FPS",
    # Performance
    "Производительность": "Desempenho",
    "Двухстадийный конвейер GPU": "Pipeline de GPU em dois estágios",
    "Быстрее на 20–30%; при нестабильности выключите": "20–30% mais rápido; desative se houver instabilidade",
    "Включён": "Ativado",
    "Чтение данных GPU процессором": "Leitura de dados da GPU pela CPU",
    "Выключены": "Desativado",
    # Developer
    "Для разработчика": "Desenvolvedor",
    "Режим работы": "Modo",
    "Новая: видеокарта работает с памятью игры напрямую, как в игре для ПК, а команды графики переводятся, а не эмулируются. Старая — модель памяти 0.3 со всеми исправлениями. Если драйвер не проходит проверку при запуске — старая":
        "O novo: a GPU usa a memória do jogo diretamente, como em um jogo de PC, e os comandos gráficos são traduzidos em vez de emulados. O antigo: o modelo de memória da 0.3 com todas as correções. Se o driver falhar na verificação inicial, o antigo",
    "Модель памяти и трансляции": "Modelo de memória e tradução",
    "Авто: новая на AMD, старая на других": "Automático: novo na AMD, antigo nas outras",
    "Новая": "Novo",
    "Старая (как в 0.3)": "Antigo (como na 0.3)",
    "Синхронизация как в 0.3": "Sincronização como na 0.3",
    "Для поиска регрессий: старая модель памяти и ожидания копий как в релизе 0.3":
        "Para encontrar regressões: o modelo de memória antigo e as esperas de cópias como na versão 0.3",
    "Статистика кадров в журнале": "Estatísticas de quadros no log",
    "Профиль GPU в журнале": "Perfil da GPU no log",
    "Слои валидации Vulkan": "Camadas de validação do Vulkan",
    "Сильно замедляет": "Muito mais lento",
    "Доп. переменные (ИМЯ=значение через пробел)": "Variáveis extras (NOME=valor, separadas por espaço)",
    # Add to Steam
    "Добавить в Steam": "Adicionar ao Steam",
    "Игра в библиотеке Steam запускается сразу, с настройками этого лаунчера": "Na biblioteca do Steam o jogo inicia direto, com as configurações deste launcher",
    "Добавить": "Adicionar",
    "Steam не найден (или в него ещё никто не входил)": "O Steam não foi encontrado (ou ninguém entrou nele ainda)",
    "Закройте Steam и нажмите «Добавить» ещё раз": "Feche o Steam e clique em Adicionar de novo",
    "Пока игра добавляется, Steam нужно закрыть; потом он запустится снова. Закрыть Steam?": "O Steam precisa fechar enquanto o jogo é adicionado; depois ele abre de novo. Fechar o Steam?",
    "Отмена": "Cancelar",
    "Закрыть Steam": "Fechar o Steam",
    "Steam не закрылся. Закройте его сами и попробуйте ещё раз": "O Steam não fechou. Feche-o você mesmo e tente de novo",
    "Не удалось добавить игру в Steam: {}": "Não foi possível adicionar o jogo ao Steam: {}",
    # Online page
    "Онлайн": "Online",
    "Играть онлайн": "Jogar online",
    "Выключено: игра остаётся офлайн, как раньше": "Desligado: o jogo continua offline, como antes",
    "Учётная запись": "Conta",
    "Пароль": "Senha",
    "Соединение": "Conexão",
    "Проверить соединение": "Testar a conexão",
    "Проверить": "Testar",
    "Сервер shadNet": "Servidor shadNet",
    "Проверка…": "Verificando…",
    "доступен": "acessível",
    "недоступен": "inacessível",
    # Button prompts
    "Применяется при запуске игры": "Aplicado ao iniciar o jogo",
    "Поменять местами A и B": "Trocar A e B",
    "Для контроллеров в стиле Nintendo: подтверждение на A, отмена на B. Применяется при запуске игры": "Para controles no estilo Nintendo: confirmar no A, voltar no B. Aplicado ao iniciar o jogo",
    "Поменять стики местами": "Trocar os analógicos",
    "Инвертировать камеру геймпада по горизонтали": "Inverter a câmera do controle na horizontal",
    "Инвертировать камеру геймпада по вертикали": "Inverter a câmera do controle na vertical",
    "Импортировать сохранения…": "Importar saves…",
    "Импорт сохранений": "Importar saves",
    "Это копия с PS4 на флешке (sdimg_*): она зашифрована ключами консоли. Экспортируйте сохранение без шифрования на PS4 (Apollo Save Tool) или через Save Wizard": "Esta é uma cópia do PS4 para pendrive (sdimg_*): ela é criptografada com as chaves do console. Exporte o save sem criptografia no PS4 (Apollo Save Tool) ou com o Save Wizard",
    "Импортировать сохранения?": "Importar os saves?",
    "Из {} (изменены {}). Текущие сохранения сначала копируются в {}": "De {} (alterados em {}). Os saves atuais são copiados antes para {}",
    "Импортировать": "Importar",
    "Не удалось импортировать сохранения": "Não foi possível importar os saves",
    "Сохранения импортированы": "Saves importados",
    # Add to Steam with Flathub's Steam
    'Steam из Flatpak запускает игры в своей песочнице, где нет ни папки игры, ни драйверов: ярлык должен запускать игру вне её (flatpak-spawn --host). Для этого Steam нужно право org.freedesktop.Flatpak, с которым он может запускать программы в вашей системе. Выдать его?':
        'O Steam do Flatpak roda os jogos dentro da sua sandbox, que não tem a pasta do jogo nem os drivers: o atalho precisa iniciar o jogo fora dela (flatpak-spawn --host). Para isso, o Steam precisa da permissão org.freedesktop.Flatpak, que permite iniciar programas no seu sistema. Conceder?',
    'Выдать право':
        'Conceder permissão',
    'Не удалось выдать право Steam: {}':
        'Não foi possível conceder a permissão ao Steam: {}',
    "Управление":
        "Controles",
    "Геймпад":
        "Gamepad",
    "Назначение кнопок; применяется при запуске игры":
        "Atribuição de botões; aplicada quando o jogo inicia",
    "Назначить":
        "Atribuir",
    "Сбросить":
        "Redefinir",
    "{} (по умолчанию)":
        "{} (padrão)",
    "не назначено":
        "não atribuído",
    "Нажмите клавишу или кнопку… (Esc — отмена)":
        "Pressione uma tecla ou um botão… (Esc cancela)",
    "Крест":
        "Xis",
    "Круг":
        "Círculo",
    "Квадрат":
        "Quadrado",
    "Треугольник":
        "Triângulo",
    "Крестовина вверх":
        "Direcional para cima",
    "Крестовина вниз":
        "Direcional para baixo",
    "Крестовина влево":
        "Direcional para a esquerda",
    "Крестовина вправо":
        "Direcional para a direita",
    "Движение вперёд":
        "Andar para frente",
    "Движение назад":
        "Andar para trás",
    "Движение влево":
        "Andar para a esquerda",
    "Движение вправо":
        "Andar para a direita",
    "Камера вверх":
        "Câmera para cima",
    "Камера вниз":
        "Câmera para baixo",
    "Камера влево":
        "Câmera para a esquerda",
    "Камера вправо":
        "Câmera para a direita",
    "Контроллер":
        "Controle",
    "Выбранный берётся, как только подключится":
        "O escolhido é usado assim que se conectar",
    "Первый подключённый":
        "O primeiro conectado",
    "{} (не подключён)":
        "{} (não conectado)",
    "Монитор":
        "Monitor",
    "Основной":
        "Principal",
    ", основной":
        ", principal",
    "eboot.bin не читается как расшифрованный исполняемый файл PS4: сделайте дамп заново":
        "O eboot.bin não pode ser lido como um executável de PS4 descriptografado: faça o dump do jogo de novo",
    "0 — без ограничения; укажите число, чтобы ограничить FPS":
        "0: sem limite; defina um número para limitar a taxa de quadros",
    "Авто":
        "Automático",
    "Включён при 8 и более потоках процессора":
        "Ligado com 8 ou mais threads de CPU",
    "Стабильнее, но медленнее":
        "Mais estável, porém mais lento",
    "По умолчанию":
        "Padrão",
    "Фоновая загрузка в видеопамять":
        "Pré-carregamento na VRAM em segundo plano",
    "Меньше рывков при подгрузке зон":
        "Menos travadas ao carregar as áreas",
    "Обычная":
        "Normal",
    "Без лишней видеопамяти":
        "Sem VRAM extra",
    "Полная":
        "Completo",
    "Около 3 ГБ видеопамяти сверху":
        "Cerca de 3 GB a mais de VRAM",
    "Выключена":
        "Desligado",
    "Сохранять журнал и статистику в файл":
        "Salvar o registro e as estatísticas em um arquivo",
    "Диагностика вылетов":
        "Diagnóstico de travamentos",
    "Проверяет кучу игры и записывает записи в её память; немного медленнее":
        "Verifica o heap do jogo e registra as escritas na memória dele; um pouco mais lento",
    "В папку logs в каталоге данных: для разбора рывков и вылетов":
        "Na pasta logs do diretório de dados: para investigar engasgos e travamentos",
    "О программе":
        "Sobre",
    "Сначала закройте игру":
        "Feche o jogo primeiro",
    "Основано на bbport от deadinside28":
        "Baseado no bbport de deadinside28",
    "Лицензия":
        "Licença",
    'GNU GPL v2 или новее · Файлы игры не входят.': 'GNU GPL v2 ou posterior · Não inclui arquivos do jogo.',
    # 0.51: mouse look, choosing NVIDIA's DLSS library, the online module
    'DLSS {}: готово':
        'DLSS {}: pronto',
    'DLSS найден (нужна видеокарта NVIDIA RTX)':
        'DLSS encontrado (requer uma GPU NVIDIA RTX)',
    'DLSS не найден: выберите библиотеку NVIDIA ниже (и нужна сборка с мостом DLSS). Игра включит FSR 3.1':
        'DLSS não encontrado: escolha a biblioteca da NVIDIA abaixo (também é preciso uma build com a ponte do DLSS). O jogo usará FSR 3.1',
    'DLSS: библиотека NVIDIA':
        'DLSS: biblioteca da NVIDIA',
    '{} — библиотека DLSS для Windows; на Linux NVIDIA её не загружает. Нужна libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        '{} é a biblioteca do DLSS para Windows; o driver da NVIDIA para Linux não a carrega. É preciso libnvidia-ngx-dlss.so.<versão> do DLSS SDK da NVIDIA: {}',
    'Библиотека DLSS NVIDIA (libnvidia-ngx-dlss.so.*)':
        'Biblioteca DLSS da NVIDIA (libnvidia-ngx-dlss.so.*)',
    'Выбрать файл…':
        'Escolher arquivo…',
    'Из сборки: {}':
        'Desta build: {}',
    'Инвертировать мышь по вертикали':
        'Inverter o eixo Y do mouse',
    'Камера мышью':
        'Câmera com o mouse',
    'Клавиатура и мышь':
        'Teclado e mouse',
    'Не удалось прочитать файл':
        'Não foi possível ler o arquivo',
    'Не удалось скопировать библиотеку':
        'Não foi possível copiar a biblioteca',
    'Нет: выберите libnvidia-ngx-dlss.so.* из DLSS SDK NVIDIA ({})':
        'Nenhuma: escolha libnvidia-ngx-dlss.so.* do DLSS SDK da NVIDIA ({})',
    'Нужен файл libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        'É preciso libnvidia-ngx-dlss.so.<versão> do DLSS SDK da NVIDIA: {}',
    'Нужна библиотека для Linux':
        'É preciso uma biblioteca para Linux',
    'Своя: {}':
        'A sua: {}',
    'Убрать выбранную':
        'Remover a escolhida',
    'Чувствительность мыши':
        'Sensibilidade do mouse',
    'Щелчок в окне игры захватывает мышь, F1 — отпускает':
        'Um clique na janela do jogo captura o mouse; F1 o libera',
    'Эта сборка без модуля онлайна (libbbnet.so): игра только офлайн':
        'Esta build não tem o módulo online (libbbnet.so): só é possível jogar offline',
    'Эта сборка без моста DLSS (libbbport_dlss.so): DLSS работать не будет':
        'Esta build não tem a ponte do DLSS (libbbport_dlss.so): o DLSS não vai funcionar',
    'Это не библиотека DLSS':
        'Esta não é a biblioteca do DLSS',
    # Online page: the server
    'Адрес сервера (host:port)':
        'Endereço do servidor (host:porta)',
    'Сервер shadNet':
        'Servidor shadNet',
    # Trophies page
    'В дампе игры нет трофеев (sce_sys/trophy)':
        'O dump do jogo não tem troféus (sce_sys/trophy)',
    'Записываются, когда игра их открывает, и показываются в игре':
        'Registrados quando o jogo os desbloqueia, e mostrados no jogo',
    'Ключ трофеев':
        'Chave de troféus',
    'Неверный ключ трофеев: названия недоступны':
        'Chave de troféus incorreta: os nomes não estão disponíveis',
    'Получен {}':
        'Conquistado em {}',
    'Получено {} из {}':
        '{} de {} conquistados',
    'Скрытый трофей':
        'Troféu oculto',
    'Трофеи':
        'Troféus',
    'Платиновый':
        'Platina',
    'Золотой':
        'Ouro',
    'Серебряный':
        'Prata',
    'Бронзовый':
        'Bronze',
    "Вход в shadNet": "Login no shadNet",
    "неверное имя или пароль": "nome ou senha incorretos",
    "такой учётной записи нет на этом сервере": "essa conta não existe neste servidor",
    "эта учётная запись уже в сети (игра запущена?)": "esta conta já está conectada (o jogo está aberto?)",
    "вход выполнен": "login feito",
    "вход не удался ({})": "falha no login ({})",
    # About: Thanks
    'Благодарности': 'Agradecimentos',
    'Без них ничего этого не было бы': 'Sem eles, nada disto seria possível',
    'Порт и его код': 'O port e seu código',
    'Помощь и тесты': 'Ajuda e testes',
    'Другие благодарности': 'Também agradecemos a',
    'bbport — порт, на котором построен весь этот проект': 'bbport, o port em que todo este projeto se baseia',
    'Игра по сети, DLSS, страница читов, добавление в Steam, значок, пропуск конвейеров, которые драйвер не может создать, и игра без вылета при нехватке видеопамяти': 'Jogo online, DLSS, a página de trapaças, Adicionar à Steam, o ícone, pular pipelines que o driver não consegue criar e nenhum travamento quando a memória de vídeo acaba',
    'Собрал и адаптировал десятки исправлений: вылеты при загрузке, чёрные изображения, апскейлер, строка производительности в журнале': 'Reuniu e adaptou dezenas de correções: travamentos ao carregar, imagens pretas, o upscaler, a linha de desempenho no log',
    'Чёрный предпросмотр персонажа, картинка экрана загрузки и память кэша текстур': 'A prévia do personagem preta, a imagem da tela de carregamento e a memória do cache de texturas',
    'Кэш текстур вовремя освобождает видеопамять': 'O cache de texturas libera a memória de vídeo a tempo',
    'Вылеты при загрузке областей': 'Travamentos ao carregar áreas',
    'Интерфейс, пропадавший не в 1080p, векторы движения больших чудовищ и ошибка памяти': 'A interface que sumia fora de 1080p, vetores de movimento das grandes feras e uma falha de memória',
    'Вылеты при загрузке некоторых карт и меню жестов с клавиатуры': 'Travamentos ao carregar alguns mapas e o menu de gestos pelo teclado',
    'Экранная клавиатура для имени персонажа и уведомление о компиляции шейдеров': 'O teclado na tela para o nome do personagem e o aviso de compilação de shaders',
    'Сетевые библиотеки игры по сети и сервер для своего кооператива': 'As bibliotecas do jogo online e o servidor para o seu próprio cooperativo',
    'Основа поддержки DLSS и модель FSR 4 без шлейфов за персонажами': 'A base do suporte a DLSS e o modelo do FSR 4 sem rastros atrás dos personagens',
    'Апскейлер FSR 3.1': 'O upscaler FSR 3.1',
    'Игра запускается, когда DLSS нельзя использовать': 'O jogo inicia quando o DLSS não pode ser usado',
    'Перевод на упрощённый китайский': 'A tradução para chinês simplificado',
    'Звук игры на полной громкости': 'O áudio do jogo em volume total',
    'Флажки и ползунки внутриигрового меню': 'As caixas de seleção e os controles deslizantes do menu do jogo',
    'Подробные отчёты с журналами и проверка исправлений': 'Relatórios detalhados com logs e teste das correções',
    'Идея поменять местами A и B на контроллерах в стиле Nintendo': 'A ideia de trocar A e B em controles no estilo Nintendo',
    'Проверка исправления видеопамяти': 'Teste da correção de memória de vídeo',
    'Рендерер и компилятор шейдеров': 'O renderizador e o recompilador de shaders',
    'Инструмент для сборки AppImage': 'A ferramenta que gera a AppImage',
    'Нашёл ошибку, из-за которой игра не запускалась на некоторых видеокартах, и ускорение камеры на DualShock 4': 'Encontrou o erro que impedia o jogo de iniciar em algumas placas de vídeo, e a aceleração da câmera no DualShock 4',
    'Нашёл, почему игра не запускалась в игровом режиме Steam Deck': 'Descobriu por que o jogo não iniciava no Modo de Jogo do Steam Deck',
    'Нашёл, при каких эффектах зависают загрузки на NVIDIA': 'Descobriu quais efeitos travam as telas de carregamento na NVIDIA',
    'ps4-pkg-extractor: установка игры из файлов .pkg': 'ps4-pkg-extractor: instalar o jogo a partir de arquivos .pkg',
    # Shader cache
    'Кэш шейдеров': 'Cache de shaders',
    'Очистить': 'Limpar',
    '{}. Если после обновления картинка выглядит странно, очистите его: шейдеры соберутся заново (первые минуты в каждой зоне возможны рывки)': '{}. Se a imagem parecer estranha após uma atualização, limpe-o: os shaders são gerados de novo (pode haver travadas nos primeiros minutos de cada área)',
    'Пусто: шейдеры соберутся при игре': 'Vazio: os shaders são gerados enquanto você joga',
    'Очистить кэш шейдеров?': 'Limpar o cache de shaders?',
    'Игра соберёт шейдеры заново: первые минуты в каждой зоне возможны рывки. Сохранения и настройки не затрагиваются.': 'O jogo gera os shaders de novo: pode haver travadas nos primeiros minutos de cada área. Saves e configurações não são afetados.',
    'Названия трофеев на английском без ключа и звук при получении трофея': 'Nomes dos troféus em inglês sem a chave e o som ao conquistar um',
    'Буфер трафарета, в который писали цветные изображения': 'O buffer de estêncil em que imagens de cor escreviam',
    'Вход на публичный сервер shadNet без отключения': 'Continuar conectado no servidor público do shadNet',
    'Установить из PKG': 'Instalar a partir de PKG',
    'Выбрать .pkg…': 'Escolher .pkg…',
    'Файлы .pkg: игра, обновление, DLC': 'Arquivos .pkg: jogo, atualização, DLC',
    'Куда установить игру': 'Onde instalar o jogo',
    'Установка…': 'Instalando…',
    'Игра установлена: {}': 'Jogo instalado: {}',
    'Не удалось установить: подробности в журнале': 'Não foi possível instalar: detalhes no registro',
    'Выход из игры из меню с контроллера, меню в пределах экрана и половины тачпада на Xbox': 'Sair do jogo pelo menu com o controle, o menu dentro da tela e as metades do touchpad no controle Xbox',
    'Вылет видеоплеера при его остановке': 'Um travamento do reprodutor de vídeo ao parar',
    'Язык внутриигрового меню при запуске без окна лаунчера': 'O idioma do menu do jogo ao iniciar sem a janela do launcher',
    'DLSS в AppImage на NVIDIA': 'DLSS no AppImage em NVIDIA',
    'Сверхширокие мониторы без растянутой картинки': 'Monitores ultrawide sem imagem esticada',
    'Движение с клавиатуры: круглая диагональ и последняя нажатая клавиша': 'Movimento pelo teclado: diagonal redonda e a última tecla pressionada',
    'Отладка вылетов: процесс ждёт отладчик (BB_FAULT_WAIT)': 'Depuração de travamentos: o processo espera um depurador (BB_FAULT_WAIT)',
    'Видеопамять на картах с 4 ГБ и вылеты: флипы, swapchain, дескрипторы и ошибки страниц; смена стиков и инверсия камеры, импорт сохранений, выбор версии': 'Memória de vídeo em placas de 4 GB e travamentos: flips, swapchain, descritores e falhas de página; troca dos analógicos e inversão da câmera, importação de saves, seletor de versão',
    'Большие группы команд записи и swapchain после изменений экрана': 'Grandes grupos de comandos gravados e a swapchain após mudanças de tela',
    # GODZILLA (gzport)
    'GODZILLA {}, версия 1.01':
        'GODZILLA {}, versão 1.01',
    'GODZILLA добавлена в библиотеку Steam':
        'GODZILLA adicionado à biblioteca da Steam',
    'GODZILLA — товарный знак Toho Co., Ltd.; игра для PS4 издана Bandai Namco Entertainment. Этот проект с ними не связан.':
        'GODZILLA é uma marca registrada da Toho Co., Ltd.; o jogo de PS4 foi publicado pela Bandai Namco Entertainment. Este projeto não tem ligação com elas.',
    'XML-патчи в формате shadPS4 для версии 01.01 из папки патчей. Применяются при запуске.':
        'Patches XML no formato do shadPS4 para a versão 01.01, carregados da pasta de patches. Aplicados ao iniciar.',
    'eboot.bin не от версии 1.01: скопируйте eboot.bin из дампа обновления 1.01 в папку игры с заменой':
        'O eboot.bin não é da 1.01: copie o eboot.bin do dump da atualização 1.01 para a pasta do jogo, substituindo-o',
    'gzport — нативный порт для Linux':
        'gzport — port nativo para Linux',
    'Авторы bbport и bloodborne_linux, на которых построен gzport, и все, кто им помогал':
        'Os autores do bbport e do bloodborne_linux, sobre os quais o gzport foi construído, e todos que os ajudaram',
    'В папке игры нет: {}. Распакуйте игру и обновление 1.01 заново':
        'Faltam na pasta do jogo: {}. Extraia o jogo e a atualização 1.01 de novo',
    'В этой папке нет сохранений GODZILLA (SAVEDATA00 с DATA.BIN)':
        'Não há saves do GODZILLA nesta pasta (SAVEDATA00 com DATA.BIN)',
    'Игра идёт с 60 FPS, как на PS4. Выше 60 FPS: нужен патч частоты кадров, его пока нет':
        'O jogo roda a 60 FPS, como no PS4. Acima de 60 FPS precisa de um patch de taxa de quadros, ainda indisponível',
    'Для GODZILLA пока недоступен: игра рисует кадр прямо в разрешении вывода':
        'Ainda indisponível para GODZILLA: o jogo desenha o quadro na própria resolução de saída',
    'Игра, обновление 1.01 и DLC из ваших файлов .pkg':
        'O jogo, a atualização 1.01 e as DLC dos seus arquivos .pkg',
    'Ключ трофеев PS4 (TrophyKey в shadPS4), 32 шестнадцатеричных символа: с ним названия и описания на языке игры. Хранится на этом компьютере. Без него видны только значки':
        'A chave de troféus do PS4 (TrophyKey no shadPS4), 32 dígitos hexadecimais: com ela, os nomes e as descrições ficam no idioma do jogo. Fica neste computador. Sem ela, só os ícones aparecem',
    'Нативный порт для Linux, версия {}':
        'Port nativo para Linux, versão {}',
    'Нужен патч для версии 1.01, его пока нет':
        'Precisa de um patch para a versão 1.01, ainda indisponível',
    'Нужно обновление 1.01: скопируйте файлы дампа обновления 1.01 в папку игры с заменой (найдена версия {})':
        'É preciso a atualização 1.01: copie o dump da atualização 1.01 para a pasta do jogo, substituindo os arquivos (versão encontrada: {})',
    'Основано на bloodborne_linux от ayozetr':
        'Baseado no bloodborne_linux de ayozetr',
    'bloodborne_linux: порт для Linux, на котором построен gzport':
        'bloodborne_linux: o port para Linux sobre o qual o gzport foi construído',
    'Папка с сохранениями GODZILLA':
        'Pasta com saves do GODZILLA',
    'Патчи игры':
        'Patches do jogo',
    'Португальский (Бразилия)':
        'Português (Brasil)',
    'Это не GODZILLA (найдено {}): нужна GODZILLA (CUSA02046) с обновлением 1.01':
        'Isto não é o GODZILLA (encontrado: {}): é preciso o GODZILLA (CUSA02046) com a atualização 1.01',
    'Тачпад, левая половина':
        'Touchpad, metade esquerda',
    'Тачпад, правая половина':
        'Touchpad, metade direita',
    'Настройки по умолчанию':
        'Padrões',
    'Восстановить мои настройки по умолчанию':
        'Restaurar meus padrões',
    'Вернуть':
        'Restaurar',
    'Сохранить текущие как мои настройки по умолчанию':
        'Salvar as atuais como meus padrões',
    'Настройки лаунчера и bbport.ini, без назначений кнопок':
        'Configurações do launcher e do bbport.ini, sem os mapeamentos de botões',
    'Сохранить':
        'Salvar',
    'Из {}':
        'De {}',
    'Своих настроек по умолчанию пока нет: восстанавливаются встроенные (папки и ключ трофеев не меняются)':
        'Você ainda não tem padrões próprios: os padrões internos são restaurados (as pastas e a chave de troféus ficam)',
    'Не удалось прочитать {}':
        'Não foi possível ler {}',
    'Восстановить настройки по умолчанию?':
        'Restaurar os padrões?',
    'Настройки лаунчера и bbport.ini станут такими, как в {}. Остальные строки bbport.ini, в том числе назначения кнопок, не меняются':
        'As configurações do launcher e do bbport.ini passam a ser as de {}. As outras linhas do bbport.ini, incluindo os mapeamentos de botões, não mudam',
    'Своих настроек по умолчанию нет: настройки лаунчера и bbport.ini станут встроенными. Папки, ключ трофеев и назначения кнопок не меняются':
        'Você não tem padrões próprios: as configurações do launcher e do bbport.ini voltam às internas. As pastas, a chave de troféus e os mapeamentos de botões não mudam',
    'Настройки по умолчанию восстановлены':
        'Padrões restaurados',
    'Сохранить текущие настройки как свои по умолчанию?':
        'Salvar as configurações atuais como seus padrões?',
    'Они запишутся в {} вместо прежних, и «Вернуть» будет восстанавливать их':
        'Elas são gravadas em {} no lugar das anteriores, e “Restaurar” volta a elas',
    'Не удалось сохранить {}':
        'Não foi possível salvar {}',
    'Текущие настройки сохранены как ваши по умолчанию':
        'Configurações atuais salvas como seus padrões',
    # Online page (LAN versus)
    "Версус по локальной сети: VS MODE в меню «Онлайн» игры, через ваш сервер shadNet (shadnet-p2p с патчем gzport). У каждого игрока своя учётная запись на этом сервере": "Versus pela rede local: VS MODE no menu «Online» do jogo, pelo seu próprio servidor shadNet (shadnet-p2p com o patch do gzport). Cada jogador tem sua própria conta nesse servidor",
    "Как настроить версус по сети": "Como configurar o versus em rede",
    "Имя учётной записи на сервере shadNet (оно же ваше имя в игре) и её пароль. Пароль хранится на этом компьютере вместе с настройками лаунчера": "O nome da sua conta no servidor shadNet (também o seu nome no jogo) e a senha dela. A senha fica salva neste computador com as configurações do launcher",
    "Порт P2P (UDP)": "Porta P2P (UDP)",
    "Через него игроки соединяются напрямую; он должен быть открыт между компьютерами": "Os jogadores se conectam diretamente por ela; ela precisa estar aberta entre os computadores",
    "Укажите адрес сервера": "Informe o endereço do servidor",
    "UDP сервера shadNet": "UDP do servidor shadNet",
    "отвечает; сервер видит этот компьютер как {}": "responde; o servidor vê este computador como {}",
    "не отвечает: матч не соединится": "sem resposta: a partida não vai se conectar",
}


# Spanish (Spain).
ES = {
    "Папка DLC": "Carpeta de DLC",
    "Выбрать папку DLC": "Elegir la carpeta de DLC",
    "Не использовать DLC": "No usar DLC",
    "Найдено DLC: {}": "DLC encontrados: {}",
    "Не используется": "Sin usar",
    "Нет DLC этой игры в папке": "No hay DLC de este juego en la carpeta",
    "Запустить": "Jugar",
    "Остановить": "Detener",
    "Настройки": "Ajustes",
    "Журнал": "Registro",
    "Не удалось запустить: {}": "No se pudo iniciar: {}",
    "\n— игра завершилась (код {}) —\n": "\n— el juego ha terminado (código {}) —\n",
    "Язык лаунчера": "Idioma del launcher",
    "Как в системе": "Sistema",
    "Применится после перезапуска лаунчера, пока игра запущена": "Se aplica al reiniciar el launcher mientras el juego está en ejecución",
    "Игра": "Juego",
    "Папка игры ({})": "Carpeta del juego ({})",
    "Папка игры": "Carpeta del juego",
    "Выбрать папку с eboot.bin": "Elige la carpeta con eboot.bin",
    "Открыть в файловом менеджере": "Abrir en el gestor de archivos",
    "Папка сохранений": "Carpeta de partidas guardadas",
    "Выбрать папку сохранений": "Elige la carpeta de partidas guardadas",
    "Вернуть папку по умолчанию": "Volver a la carpeta predeterminada",
    "Язык системы": "Idioma del sistema",
    "По умолчанию: {}": "Predeterminado: {}",
    "Найдены сохранения": "Partidas guardadas encontradas",
    "Сохранений пока нет: игра создаст их здесь": "Aún no hay partidas guardadas: el juego las creará aquí",
    "не выбрана": "sin elegir",
    "Нет eboot.bin в папке": "No hay eboot.bin en la carpeta",
    "Управление": "Controles",
    "Геймпад": "Mando",
    "Назначение кнопок; применяется при запуске игры": "Asignación de botones; se aplica al iniciar el juego",
    "Назначить": "Asignar",
    "Сбросить": "Restablecer",
    "{} (по умолчанию)": "{} (predeterminado)",
    "не назначено": "sin asignar",
    "Нажмите клавишу или кнопку… (Esc — отмена)": "Pulsa una tecla o un botón… (Esc cancela)",
    "Крест": "Cruz",
    "Круг": "Círculo",
    "Квадрат": "Cuadrado",
    "Треугольник": "Triángulo",
    "Крестовина вверх": "Cruceta arriba",
    "Крестовина вниз": "Cruceta abajo",
    "Крестовина влево": "Cruceta izquierda",
    "Крестовина вправо": "Cruceta derecha",
    "Движение вперёд": "Avanzar",
    "Движение назад": "Retroceder",
    "Движение влево": "Moverse a la izquierda",
    "Движение вправо": "Moverse a la derecha",
    "Камера вверх": "Cámara arriba",
    "Камера вниз": "Cámara abajo",
    "Камера влево": "Cámara a la izquierda",
    "Камера вправо": "Cámara a la derecha",
    "Контроллер": "Mando",
    "Выбранный берётся, как только подключится": "Se usa el elegido en cuanto se conecta",
    "Первый подключённый": "El primero conectado",
    "{} (не подключён)": "{} (no conectado)",
    "eboot.bin не читается как расшифрованный исполняемый файл PS4: сделайте дамп заново": "No se puede leer eboot.bin como ejecutable de PS4 descifrado: vuelve a volcar el juego",
    "Папка игры (с eboot.bin)": "Carpeta del juego (con eboot.bin)",
    "Английский": "Inglés",
    "Русский": "Ruso",
    "Французский": "Francés",
    "Испанский": "Español",
    "Обновить список": "Actualizar la lista",
    "Сторонние патчи": "Parches de terceros",
    "Папка патчей": "Carpeta de parches",
    "Выбрать папку патчей": "Elige la carpeta de parches",
    "Открыть папку патчей": "Abrir la carpeta de parches",
    "Патчей нет": "Ningún parche",
    "Автор: {}": "Autor: {}",
    "Экран": "Pantalla",
    "Разрешение вывода": "Resolución de salida",
    "Апскейлер дорисовывает кадр; Steam Deck — 720p": "El escalador rellena el fotograma; Steam Deck: 720p",
    "Полноэкранный режим": "Pantalla completa",
    "Смена разрешения на лету": "Cambio de resolución en tiempo real",
    "Без перезапуска, но медленнее на Steam Deck и старых GPU": "No requiere reinicio, pero es más lento en la Steam Deck y en GPU antiguas",
    "Авто (по видеокарте)": "Automático (según la GPU)",
    "Выключена (быстрее)": "Desactivado (más rápido)",
    "Включена": "Activado",
    "Режим показа кадров": "Modo de presentación",
    "Разрешить HDR": "Permitir HDR",
    "Апскейлер": "Escalador",
    "Хранится в bbport.ini; в игре меняется через меню (Insert или L3+R3)": "Se guarda en bbport.ini; dentro del juego, cámbialo en el menú (Insert o L3+R3)",
    "TAA (нативное сглаживание)": "TAA (antialiasing nativo)",
    "Выключен": "Desactivado",
    "Пресет": "Preajuste",
    "Резкость (RCAS)": "Nitidez (RCAS)",
    "Сила резкости": "Intensidad de nitidez",
    "Векторы движения объектов": "Vectores de movimiento de objetos",
    "Меньше гостинга на персонажах; стоит около 10% FPS": "Menos ghosting en los personajes; cuesta alrededor del 10 % de FPS",
    "Показывать FPS": "Mostrar FPS",
    "Ассеты найдены": "Recursos encontrados",
    "Нет ассетов: tools/fetch_fsr4_assets.sh": "Faltan los recursos: tools/fetch_fsr4_assets.sh",
    "Ассеты для выбранного режима найдены": "Recursos del modo seleccionado encontrados",
    "{}. Соберите FSR 4.1.1 из своей DLL кнопкой «Выбрать DLL…» ниже": "{}. Genera FSR 4.1.1 a partir de tu propia DLL con el botón «Elegir DLL…» de abajo",
    "FSR 4.1.1 из своей DLL AMD": "FSR 4.1.1 desde tu propia DLL de AMD",
    "Отменить": "Cancelar",
    "Выбрать DLL…": "Elegir DLL…",
    "DLL апскейлера AMD (amd_fidelityfx_upscaler_dx12.dll)": "DLL del escalador de AMD (amd_fidelityfx_upscaler_dx12.dll)",
    "нет": "ninguno",
    "Эта DLL не подходит": "Esta DLL no sirve",
    "{}: версия {}, модели FSR 4: {}.\n\nbbport повторяет только официальную FSR 4.1.x от AMD (модель v07_fp8_no_scale): например, FSR4_LATEST из OptiScaler или amd_fidelityfx_upscaler_dx12.dll из игры с FSR 4.1. Сборки сообщества (4.0.2b и подобные) устроены иначе и пока не поддерживаются.": "{}: versión {}, modelos de FSR 4: {}.\n\nbbport solo reproduce el FSR 4.1.x oficial de AMD (modelo v07_fp8_no_scale): por ejemplo, FSR4_LATEST de OptiScaler o amd_fidelityfx_upscaler_dx12.dll de un juego con FSR 4.1. Las compilaciones de la comunidad (4.0.2b y similares) tienen otra estructura y todavía no se admiten.",
    "Загрузчик не подходит": "El cargador no sirve",
    "Загрузчик FidelityFX (amd_fidelityfx_loader_dx12.dll или amd_fidelityfx_dx12.dll)": "Cargador de FidelityFX (amd_fidelityfx_loader_dx12.dll o amd_fidelityfx_dx12.dll)",
    "\n— сборка FSR 4.1.1 из {} —\n": "\n— generando FSR 4.1.1 a partir de {} —\n",
    "Подготовка…": "Preparando…",
    "Запись проходов DLL под Proton: {} из {}": "Grabando las pasadas de la DLL en Proton: {} de {}",
    "Перевод проходов в SPIR-V…": "Traduciendo las pasadas a SPIR-V…",
    "— сборка FSR 4.1.1 завершилась (код {}) —\n": "— Generación de FSR 4.1.1 terminada (código {}) —\n",
    "FSR 4.1.1 собран и выбран": "FSR 4.1.1 generado y seleccionado",
    "Сборка FSR 4.1.1 отменена": "Generación de FSR 4.1.1 cancelada",
    "FSR 4.1.1 не собран": "No se generó FSR 4.1.1",
    "DLL не подходит: подробности в журнале": "La DLL no sirve: detalles en el registro",
    "Не хватает программ для сборки: список в журнале": "Faltan herramientas para la generación: la lista está en el registro",
    "Записанные проходы не совпали с тем, что повторяет bbport (другая версия DLL или новая видеокарта?): подробности в журнале": "Las pasadas grabadas no coinciden con lo que reproduce bbport (¿otra versión de la DLL o una GPU nueva?): detalles en el registro",
    "Не найден загрузчик FidelityFX 2.x": "No se encontró ningún cargador de FidelityFX 2.x",
    "Не найден подходящий Proton: установите GE-Proton 10 или новее (ProtonUp-Qt) или Proton Experimental / Proton-CachyOS в Steam. Если они есть — запустите в Steam любую игру с этим Proton, чтобы Steam поставил его рантайм": "No se encontró un Proton adecuado: instala GE-Proton 10 o posterior (ProtonUp-Qt), o Proton Experimental / Proton-CachyOS en Steam. Si ya los tienes, inicia cualquier juego con ese Proton en Steam para que Steam instale su runtime",
    "Ни один Proton не запустил FSR 4.1 из этой DLL. Либо они слишком старые (подходят GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), либо DLL не включает FSR 4.1 на этой видеокарте (Steam Deck?): тогда соберите на ПК с Radeon RX 7000/9000 и скопируйте папку fsr4_411. Подробности в журнале": "Ningún Proton ha podido iniciar el FSR 4.1 de esta DLL. O son demasiado antiguos (funcionan GE-Proton 10+, Proton Experimental y Proton-CachyOS 11), o la DLL no activa FSR 4.1 en esta GPU (¿Steam Deck?): en ese caso, genera en un PC con una Radeon RX 7000/9000 y copia la carpeta fsr4_411. Detalles en el registro",
    "На NixOS запись идёт на самой системе (systemd --user) через umu-launcher из nix-shell, а здесь их не нашлось: установите umu-launcher или Nix. Подробности в журнале": "En NixOS la grabación se ejecuta en el propio sistema (systemd --user) con umu-launcher de nix-shell, y no se ha encontrado ninguno de los dos: instala umu-launcher o Nix. Detalles en el registro",
    "{}: FSR {}. Это официальная FSR 4.0.x от AMD: она включается только на видеокартах RDNA4 (RX 9000), а под Proton на других видеокартах не запускается, поэтому записать её нельзя.\n\nНужна FSR 4.1.x: например, FSR4_LATEST из OptiScaler или DLL из игры с FSR 4.1.": "{}: FSR {}. Este es el FSR 4.0.x oficial de AMD: solo se activa en GPU RDNA4 (RX 9000) y no se inicia en Proton en otras GPU, por lo que no se puede grabar.\n\nHace falta FSR 4.1.x: por ejemplo, FSR4_LATEST de OptiScaler o la DLL de un juego con FSR 4.1.",
    "{}: в этой DLL нет FSR 4. Нужна amd_fidelityfx_upscaler_dx12.dll версии 4.1.x.": "{}: esta DLL no contiene FSR 4. Hace falta amd_fidelityfx_upscaler_dx12.dll versión 4.1.x.",
    "Это не загрузчик": "Este no es el cargador",
    "{} — это DLL апскейлера. Загрузчик называется amd_fidelityfx_loader_dx12.dll (у OptiScaler — amd_fidelityfx_dx12.dll) и лежит в той же папке игры, что и DLL апскейлера.": "{} es la DLL del escalador. El cargador se llama amd_fidelityfx_loader_dx12.dll (amd_fidelityfx_dx12.dll en OptiScaler) y está en la misma carpeta del juego que la DLL del escalador.",
    "{}: версия {}. Нужен загрузчик FidelityFX 2.x — из той же игры, что и DLL апскейлера.": "{}: versión {}. Hace falta un cargador de FidelityFX 2.x, del mismo juego que la DLL del escalador.",
    "Рядом с DLL нет загрузчика: выберите amd_fidelityfx_loader_dx12.dll из папки игры": "No hay cargador junto a la DLL: elige amd_fidelityfx_loader_dx12.dll de la carpeta del juego",
    "Собрать FSR 4.1.1 из amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: папка FSR4_LATEST, или из игры с FSR 4.1). Нужен GE-Proton 10+, Proton Experimental или Proton-CachyOS; 2–5 минут (RDNA4: вдвое дольше, ещё и вариант FP8)": "Genera FSR 4.1.1 a partir de amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: la carpeta FSR4_LATEST, o la de un juego con FSR 4.1). Requiere GE-Proton 10+, Proton Experimental o Proton-CachyOS; 2–5 minutos (RDNA4: el doble, con la variante FP8)",
    "Сборка не удалась (код {}): подробности в журнале": "La generación ha fallado (código {}): detalles en el registro",
    "Сглаживание в разрешении вывода без модели FSR": "Antialiasing a la resolución de salida, sin modelo FSR",
    "Нет или повреждён файл {}": "Archivo {} ausente o dañado",
    "Пропуск заставок при запуске": "Omitir los vídeos de introducción",
    "Частота кадров": "Tasa de fotogramas",
    "Режим": "Modo",
    "Какой патч частоты кадров применить к игре": "Qué parche de tasa de fotogramas aplicar al juego",
    "Без ограничения (патч)": "Sin límite (parche)",
    "60 (как на PS4)": "60 (como en PS4)",
    "Ограничение FPS": "Límite de FPS",
    "0 — без ограничения; укажите число, чтобы ограничить FPS": "0: sin límite; indica un número para limitar la tasa de fotogramas",
    "Производительность": "Rendimiento",
    "Двухстадийный конвейер GPU": "Pipeline de GPU en dos etapas",
    "Быстрее на 20–30%; при нестабильности выключите": "Un 20–30 % más rápido; desactívalo si hay inestabilidad",
    "Авто": "Automático",
    "Включён при 8 и более потоках процессора": "Activado con 8 o más hilos de CPU",
    "Включён": "Activado",
    "Стабильнее, но медленнее": "Más estable, pero más lento",
    "Чтение данных GPU процессором": "Lectura de datos de la GPU por la CPU",
    "По умолчанию": "Predeterminado",
    "Фоновая загрузка в видеопамять": "Precarga en segundo plano en la VRAM",
    "Меньше рывков при подгрузке зон": "Menos tirones al cargar zonas",
    "Обычная": "Normal",
    "Без лишней видеопамяти": "Sin VRAM adicional",
    "Полная": "Completa",
    "Около 3 ГБ видеопамяти сверху": "Unos 3 GB más de VRAM",
    "Режим работы": "Modo",
    "Синхронизация как в 0.3": "Sincronización como en la 0.3",
    "Для поиска регрессий: старая модель памяти и ожидания копий как в релизе 0.3": "Para encontrar regresiones: el modelo de memoria antiguo y las esperas de copia tal como se publicaron en la 0.3",
    "Выключена": "Desactivado",
    "Выключены": "Desactivado",
    "Для разработчика": "Desarrollador",
    "Статистика кадров в журнале": "Estadísticas de fotogramas en el registro",
    "Сохранять журнал и статистику в файл": "Guardar el registro y las estadísticas en un archivo",
    "Диагностика вылетов": "Diagnóstico de fallos",
    "Проверяет кучу игры и записывает записи в её память; немного медленнее": "Comprueba el heap del juego y registra las escrituras en su memoria; algo más lento",
    "В папку logs в каталоге данных: для разбора рывков и вылетов": "En la carpeta logs del directorio de datos: para investigar tirones y fallos",
    "Профиль GPU в журнале": "Perfil de la GPU en el registro",
    "Слои валидации Vulkan": "Capas de validación de Vulkan",
    "Сильно замедляет": "Mucho más lento",
    "Доп. переменные (ИМЯ=значение через пробел)": "Variables adicionales (NOMBRE=valor, separadas por espacios)",
    # Add to Steam
    "Добавить в Steam": "Añadir a Steam",
    "Игра в библиотеке Steam запускается сразу, с настройками этого лаунчера": "Desde la biblioteca de Steam el juego arranca directamente, con los ajustes de este launcher",
    "Добавить": "Añadir",
    "Steam не найден (или в него ещё никто не входил)": "No se ha encontrado Steam (o nadie ha iniciado sesión todavía)",
    "Закройте Steam и нажмите «Добавить» ещё раз": "Cierra Steam y vuelve a pulsar Añadir",
    "Пока игра добавляется, Steam нужно закрыть; потом он запустится снова. Закрыть Steam?": "Steam tiene que cerrarse mientras se añade el juego; después se vuelve a abrir. ¿Cerrar Steam?",
    "Отмена": "Cancelar",
    "Закрыть Steam": "Cerrar Steam",
    "Steam не закрылся. Закройте его сами и попробуйте ещё раз": "Steam no se ha cerrado. Ciérralo tú y vuelve a intentarlo",
    "Не удалось добавить игру в Steam: {}": "No se pudo añadir el juego a Steam: {}",
    # Online page
    "Онлайн": "Online",
    "Играть онлайн": "Jugar online",
    "Выключено: игра остаётся офлайн, как раньше": "Desactivado: el juego sigue sin conexión, como antes",
    "Учётная запись": "Cuenta",
    "Пароль": "Contraseña",
    "Соединение": "Conexión",
    "Проверить соединение": "Probar la conexión",
    "Проверить": "Probar",
    "Сервер shadNet": "Servidor shadNet",
    "Проверка…": "Comprobando…",
    "доступен": "accesible",
    "недоступен": "no accesible",
    # Button prompts
    "Применяется при запуске игры": "Se aplica al iniciar el juego",
    "Поменять местами A и B": "Intercambiar A y B",
    "Для контроллеров в стиле Nintendo: подтверждение на A, отмена на B. Применяется при запуске игры": "Para mandos estilo Nintendo: confirmar con A, volver con B. Se aplica al iniciar el juego",
    "Поменять стики местами": "Intercambiar los sticks",
    "Инвертировать камеру геймпада по горизонтали": "Invertir la cámara del mando en horizontal",
    "Инвертировать камеру геймпада по вертикали": "Invertir la cámara del mando en vertical",
    "Импортировать сохранения…": "Importar partidas…",
    "Импорт сохранений": "Importar partidas",
    "Это копия с PS4 на флешке (sdimg_*): она зашифрована ключами консоли. Экспортируйте сохранение без шифрования на PS4 (Apollo Save Tool) или через Save Wizard": "Es una copia de PS4 para memoria USB (sdimg_*): está cifrada con las claves de la consola. Exporta la partida sin cifrar en la PS4 (Apollo Save Tool) o con Save Wizard",
    "Импортировать сохранения?": "¿Importar las partidas?",
    "Из {} (изменены {}). Текущие сохранения сначала копируются в {}": "Desde {} (modificadas el {}). Las partidas actuales se copian antes a {}",
    "Импортировать": "Importar",
    "Не удалось импортировать сохранения": "No se pudieron importar las partidas",
    "Сохранения импортированы": "Partidas importadas",
    # Add to Steam with Flathub's Steam
    'Steam из Flatpak запускает игры в своей песочнице, где нет ни папки игры, ни драйверов: ярлык должен запускать игру вне её (flatpak-spawn --host). Для этого Steam нужно право org.freedesktop.Flatpak, с которым он может запускать программы в вашей системе. Выдать его?':
        'El Steam de Flatpak ejecuta los juegos dentro de su sandbox, donde no están ni la carpeta del juego ni los drivers: el atajo tiene que arrancar el juego fuera de ella (flatpak-spawn --host). Para eso Steam necesita el permiso org.freedesktop.Flatpak, que le permite ejecutar programas en tu sistema. ¿Concederlo?',
    'Выдать право':
        'Conceder permiso',
    'Не удалось выдать право Steam: {}':
        'No se pudo conceder el permiso a Steam: {}',
    "Копировать":
        "Copiar",
    "Экспорт журнала…":
        "Exportar registro…",
    "Экспорт журнала":
        "Exportar registro",
    "Журнал скопирован":
        "Registro copiado",
    "Журнал сохранён: {}":
        "Registro guardado: {}",
    "Не удалось сохранить журнал: {}":
        "No se pudo guardar el registro: {}",
    "Монитор":
        "Monitor",
    "Основной":
        "Principal",
    ", основной":
        ", principal",
    "Новая: видеокарта работает с памятью игры напрямую, как в игре для ПК, а команды графики переводятся, а не эмулируются. Старая — модель памяти 0.3 со всеми исправлениями. Если драйвер не проходит проверку при запуске — старая":
        "El nuevo: la tarjeta gráfica trabaja directamente con la memoria del juego, como en un juego de PC, y los comandos gráficos se traducen en vez de emularse. El antiguo: el modelo de memoria de la 0.3 con todas las correcciones. Si el controlador no pasa la comprobación al arrancar, el antiguo",
    "Модель памяти и трансляции":
        "Modelo de memoria y traducción",
    "Авто: новая на AMD, старая на других":
        "Automático: nuevo en AMD, antiguo en las demás",
    "Новая":
        "Nuevo",
    "Старая (как в 0.3)":
        "Antiguo (como en la 0.3)",
    "О программе":
        "Acerca de",
    "Сначала закройте игру":
        "Cierra el juego primero",
    "Основано на bbport от deadinside28":
        "Basado en bbport, de deadinside28",
    "Лицензия":
        "Licencia",
    'GNU GPL v2 или новее · Файлы игры не входят.': 'GNU GPL v2 o posterior · No incluye archivos del juego.',
    # 0.51: mouse look, choosing NVIDIA's DLSS library, the online module
    'DLSS {}: готово':
        'DLSS {}: listo',
    'DLSS найден (нужна видеокарта NVIDIA RTX)':
        'DLSS encontrado (necesita una GPU NVIDIA RTX)',
    'DLSS не найден: выберите библиотеку NVIDIA ниже (и нужна сборка с мостом DLSS). Игра включит FSR 3.1':
        'DLSS no encontrado: elige la biblioteca de NVIDIA abajo (también hace falta una compilación con el puente de DLSS). El juego usará FSR 3.1',
    'DLSS: библиотека NVIDIA':
        'DLSS: biblioteca de NVIDIA',
    '{} — библиотека DLSS для Windows; на Linux NVIDIA её не загружает. Нужна libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        '{} es la biblioteca de DLSS para Windows; el controlador de NVIDIA para Linux no la carga. Hace falta libnvidia-ngx-dlss.so.<versión> del DLSS SDK de NVIDIA: {}',
    'Библиотека DLSS NVIDIA (libnvidia-ngx-dlss.so.*)':
        'Biblioteca DLSS de NVIDIA (libnvidia-ngx-dlss.so.*)',
    'Выбрать файл…':
        'Elegir archivo…',
    'Из сборки: {}':
        'De esta compilación: {}',
    'Инвертировать мышь по вертикали':
        'Invertir el eje Y del ratón',
    'Камера мышью':
        'Cámara con el ratón',
    'Клавиатура и мышь':
        'Teclado y ratón',
    'Не удалось прочитать файл':
        'No se pudo leer el archivo',
    'Не удалось скопировать библиотеку':
        'No se pudo copiar la biblioteca',
    'Нет: выберите libnvidia-ngx-dlss.so.* из DLSS SDK NVIDIA ({})':
        'Ninguna: elige libnvidia-ngx-dlss.so.* del DLSS SDK de NVIDIA ({})',
    'Нужен файл libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        'Hace falta libnvidia-ngx-dlss.so.<versión> del DLSS SDK de NVIDIA: {}',
    'Нужна библиотека для Linux':
        'Hace falta una biblioteca para Linux',
    'Своя: {}':
        'La tuya: {}',
    'Убрать выбранную':
        'Quitar la elegida',
    'Чувствительность мыши':
        'Sensibilidad del ratón',
    'Щелчок в окне игры захватывает мышь, F1 — отпускает':
        'Un clic en la ventana del juego captura el ratón; F1 lo suelta',
    'Эта сборка без модуля онлайна (libbbnet.so): игра только офлайн':
        'Esta compilación no tiene el módulo online (libbbnet.so): solo se puede jugar sin conexión',
    'Эта сборка без моста DLSS (libbbport_dlss.so): DLSS работать не будет':
        'Esta compilación no tiene el puente de DLSS (libbbport_dlss.so): DLSS no funcionará',
    'Это не библиотека DLSS':
        'No es la biblioteca de DLSS',
    # Online page: the server
    'Адрес сервера (host:port)':
        'Dirección del servidor (host:puerto)',
    'Сервер shadNet':
        'Servidor shadNet',
    # Trophies page
    'В дампе игры нет трофеев (sce_sys/trophy)':
        'El volcado del juego no tiene trofeos (sce_sys/trophy)',
    'Записываются, когда игра их открывает, и показываются в игре':
        'Se guardan cuando el juego los desbloquea, y se muestran en el juego',
    'Ключ трофеев':
        'Clave de trofeos',
    'Неверный ключ трофеев: названия недоступны':
        'Clave de trofeos incorrecta: los nombres no están disponibles',
    'Получен {}':
        'Conseguido el {}',
    'Получено {} из {}':
        '{} de {} conseguidos',
    'Скрытый трофей':
        'Trofeo oculto',
    'Трофеи':
        'Trofeos',
    'Платиновый':
        'Platino',
    'Золотой':
        'Oro',
    'Серебряный':
        'Plata',
    'Бронзовый':
        'Bronce',
    "Вход в shadNet": "Inicio de sesión en shadNet",
    "неверное имя или пароль": "nombre o contraseña incorrectos",
    "такой учётной записи нет на этом сервере": "esa cuenta no existe en este servidor",
    "эта учётная запись уже в сети (игра запущена?)": "esta cuenta ya tiene la sesión iniciada (¿está el juego abierto?)",
    "вход выполнен": "sesión iniciada",
    "вход не удался ({})": "no se pudo iniciar sesión ({})",
    # About: Thanks
    'Благодарности': 'Agradecimientos',
    'Без них ничего этого не было бы': 'Sin ellos, nada de esto sería posible',
    'Порт и его код': 'El port y su código',
    'Помощь и тесты': 'Ayuda y pruebas',
    'Другие благодарности': 'También gracias a',
    'bbport — порт, на котором построен весь этот проект': 'bbport, el port en el que se basa todo este proyecto',
    'Игра по сети, DLSS, страница читов, добавление в Steam, значок, пропуск конвейеров, которые драйвер не может создать, и игра без вылета при нехватке видеопамяти': 'Juego online, DLSS, la página de trucos, Añadir a Steam, el icono, saltar los pipelines que el driver no puede crear y ningún cierre al quedarse sin memoria de vídeo',
    'Собрал и адаптировал десятки исправлений: вылеты при загрузке, чёрные изображения, апскейлер, строка производительности в журнале': 'Reunió y adaptó decenas de arreglos: cierres al cargar, imágenes en negro, el escalado, la línea de rendimiento del registro',
    'Чёрный предпросмотр персонажа, картинка экрана загрузки и память кэша текстур': 'La vista previa del personaje en negro, la imagen de la pantalla de carga y la memoria de la caché de texturas',
    'Кэш текстур вовремя освобождает видеопамять': 'Que la caché de texturas libere la memoria de vídeo a tiempo',
    'Вылеты при загрузке областей': 'Cierres al cargar zonas',
    'Интерфейс, пропадавший не в 1080p, векторы движения больших чудовищ и ошибка памяти': 'La interfaz que desaparecía fuera de 1080p, los vectores de movimiento de las bestias grandes y un fallo de memoria',
    'Вылеты при загрузке некоторых карт и меню жестов с клавиатуры': 'Cierres al cargar algunos mapas y el menú de gestos desde el teclado',
    'Экранная клавиатура для имени персонажа и уведомление о компиляции шейдеров': 'El teclado en pantalla para el nombre del personaje y el aviso de compilación de shaders',
    'Сетевые библиотеки игры по сети и сервер для своего кооператива': 'Las librerías del juego online y el servidor para el cooperativo propio',
    'Основа поддержки DLSS и модель FSR 4 без шлейфов за персонажами': 'La base del soporte de DLSS y el modelo de FSR 4 sin estelas tras los personajes',
    'Апскейлер FSR 3.1': 'El escalado FSR 3.1',
    'Игра запускается, когда DLSS нельзя использовать': 'Que el juego arranque cuando no se puede usar DLSS',
    'Перевод на упрощённый китайский': 'La traducción al chino simplificado',
    'Звук игры на полной громкости': 'El sonido del juego a volumen completo',
    'Флажки и ползунки внутриигрового меню': 'Las casillas y los deslizadores del menú del juego',
    'Подробные отчёты с журналами и проверка исправлений': 'Reportes detallados con registros y pruebas de los arreglos',
    'Идея поменять местами A и B на контроллерах в стиле Nintendo': 'La idea de cambiar A y B en mandos de estilo Nintendo',
    'Проверка исправления видеопамяти': 'Probar el arreglo de la memoria de vídeo',
    'Рендерер и компилятор шейдеров': 'El renderizador y el recompilador de shaders',
    'Инструмент для сборки AppImage': 'La herramienta que crea la AppImage',
    'Нашёл ошибку, из-за которой игра не запускалась на некоторых видеокартах, и ускорение камеры на DualShock 4': 'Encontró el fallo que impedía arrancar el juego en algunas gráficas, y la aceleración de la cámara con DualShock 4',
    'Нашёл, почему игра не запускалась в игровом режиме Steam Deck': 'Descubrió por qué el juego no arrancaba en el modo de juego de la Steam Deck',
    'Нашёл, при каких эффектах зависают загрузки на NVIDIA': 'Descubrió qué efectos congelan las pantallas de carga en NVIDIA',
    'ps4-pkg-extractor: установка игры из файлов .pkg': 'ps4-pkg-extractor: instalar el juego desde archivos .pkg',
    # Shader cache
    'Кэш шейдеров': 'Caché de shaders',
    'Очистить': 'Borrar',
    '{}. Если после обновления картинка выглядит странно, очистите его: шейдеры соберутся заново (первые минуты в каждой зоне возможны рывки)': '{}. Si la imagen se ve rara tras una actualización, bórrala: los shaders se vuelven a generar (puede haber tirones los primeros minutos en cada zona)',
    'Пусто: шейдеры соберутся при игре': 'Vacía: los shaders se generan mientras juegas',
    'Очистить кэш шейдеров?': '¿Borrar la caché de shaders?',
    'Игра соберёт шейдеры заново: первые минуты в каждой зоне возможны рывки. Сохранения и настройки не затрагиваются.': 'El juego volverá a generar los shaders: puede haber tirones los primeros minutos en cada zona. Las partidas y los ajustes no se tocan.',
    'Названия трофеев на английском без ключа и звук при получении трофея': 'Los nombres de los trofeos en inglés sin la clave y el sonido al conseguir uno',
    'Буфер трафарета, в который писали цветные изображения': 'El búfer de estarcido en el que escribían imágenes de color',
    'Вход на публичный сервер shadNet без отключения': 'Seguir conectado en el servidor público de shadNet',
    'Установить из PKG': 'Instalar desde PKG',
    'Выбрать .pkg…': 'Elegir .pkg…',
    'Файлы .pkg: игра, обновление, DLC': 'Archivos .pkg: juego, actualización, DLC',
    'Куда установить игру': 'Dónde instalar el juego',
    'Установка…': 'Instalando…',
    'Игра установлена: {}': 'Juego instalado: {}',
    'Не удалось установить: подробности в журнале': 'No se pudo instalar: detalles en el registro',
    'Выход из игры из меню с контроллера, меню в пределах экрана и половины тачпада на Xbox': 'Salir del juego desde el menú con el mando, el menú dentro de la pantalla y las mitades del panel táctil en mandos Xbox',
    'Вылет видеоплеера при его остановке': 'Un cierre del reproductor de vídeo al detenerse',
    'Язык внутриигрового меню при запуске без окна лаунчера': 'El idioma del menú del juego al arrancar sin la ventana del launcher',
    'DLSS в AppImage на NVIDIA': 'DLSS en la AppImage con NVIDIA',
    'Сверхширокие мониторы без растянутой картинки': 'Monitores ultrapanorámicos sin la imagen estirada',
    'Движение с клавиатуры: круглая диагональ и последняя нажатая клавиша': 'Movimiento con teclado: diagonal redonda y la última tecla pulsada',
    'Отладка вылетов: процесс ждёт отладчик (BB_FAULT_WAIT)': 'Depuración de cierres: el proceso espera a un depurador (BB_FAULT_WAIT)',
    'Видеопамять на картах с 4 ГБ и вылеты: флипы, swapchain, дескрипторы и ошибки страниц; смена стиков и инверсия камеры, импорт сохранений, выбор версии': 'Memoria de vídeo en tarjetas de 4 GB y cierres: flips, swapchain, descriptores y fallos de página; intercambio de sticks e inversión de la cámara, importación de partidas, selector de versión',
    'Большие группы команд записи и swapchain после изменений экрана': 'Grupos grandes de comandos grabados y el swapchain tras cambios de pantalla',
    # GODZILLA (gzport)
    'GODZILLA {}, версия 1.01':
        'GODZILLA {}, versión 1.01',
    'GODZILLA добавлена в библиотеку Steam':
        'GODZILLA añadido a la biblioteca de Steam',
    'GODZILLA — товарный знак Toho Co., Ltd.; игра для PS4 издана Bandai Namco Entertainment. Этот проект с ними не связан.':
        'GODZILLA es una marca registrada de Toho Co., Ltd.; el juego de PS4 lo publicó Bandai Namco Entertainment. Este proyecto no está afiliado a ellas.',
    'XML-патчи в формате shadPS4 для версии 01.01 из папки патчей. Применяются при запуске.':
        'Parches XML en formato shadPS4 para la versión 01.01, de la carpeta de parches. Se aplican al iniciar.',
    'eboot.bin не от версии 1.01: скопируйте eboot.bin из дампа обновления 1.01 в папку игры с заменой':
        'eboot.bin no es de la 1.01: copia eboot.bin de la actualización 1.01 volcada en la carpeta del juego, reemplazándolo',
    'gzport — нативный порт для Linux':
        'gzport — port nativo para Linux',
    'Авторы bbport и bloodborne_linux, на которых построен gzport, и все, кто им помогал':
        'Los autores de bbport y bloodborne_linux, sobre los que se construye gzport, y todos los que les ayudaron',
    'В папке игры нет: {}. Распакуйте игру и обновление 1.01 заново':
        'Faltan en la carpeta del juego: {}. Vuelve a extraer el juego y la actualización 1.01',
    'В этой папке нет сохранений GODZILLA (SAVEDATA00 с DATA.BIN)':
        'No hay partidas de GODZILLA en esta carpeta (SAVEDATA00 con DATA.BIN)',
    'Игра идёт с 60 FPS, как на PS4. Выше 60 FPS: нужен патч частоты кадров, его пока нет':
        'El juego va a 60 FPS, como en PS4. Más de 60 FPS necesita un parche de tasa de fotogramas, aún no disponible',
    'Для GODZILLA пока недоступен: игра рисует кадр прямо в разрешении вывода':
        'Aún no disponible para GODZILLA: el juego dibuja el fotograma directamente a la resolución de salida',
    'Игра, обновление 1.01 и DLC из ваших файлов .pkg':
        'El juego, la actualización 1.01 y los DLC desde tus archivos .pkg',
    'Ключ трофеев PS4 (TrophyKey в shadPS4), 32 шестнадцатеричных символа: с ним названия и описания на языке игры. Хранится на этом компьютере. Без него видны только значки':
        'La clave de trofeos de PS4 (TrophyKey en shadPS4), 32 dígitos hexadecimales: con ella, los nombres y las descripciones salen en el idioma del juego. Se guarda en este equipo. Sin ella solo se ven los iconos',
    'Нативный порт для Linux, версия {}':
        'Port nativo para Linux, versión {}',
    'Нужен патч для версии 1.01, его пока нет':
        'Necesita un parche para la versión 1.01, aún no disponible',
    'Нужно обновление 1.01: скопируйте файлы дампа обновления 1.01 в папку игры с заменой (найдена версия {})':
        'Se necesita la actualización 1.01: copia la actualización 1.01 volcada en la carpeta del juego, reemplazando los archivos (versión encontrada: {})',
    'Основано на bloodborne_linux от ayozetr':
        'Basado en bloodborne_linux de ayozetr',
    'bloodborne_linux: порт для Linux, на котором построен gzport':
        'bloodborne_linux: el port para Linux sobre el que se construye gzport',
    'Папка с сохранениями GODZILLA':
        'Carpeta con partidas de GODZILLA',
    'Патчи игры':
        'Parches del juego',
    'Португальский (Бразилия)':
        'Portugués (Brasil)',
    'Это не GODZILLA (найдено {}): нужна GODZILLA (CUSA02046) с обновлением 1.01':
        'Esto no es GODZILLA (encontrado: {}): se necesita GODZILLA (CUSA02046) con la actualización 1.01',
    'Тачпад, левая половина':
        'Panel táctil, mitad izquierda',
    'Тачпад, правая половина':
        'Panel táctil, mitad derecha',
    'Настройки по умолчанию':
        'Valores predeterminados',
    'Восстановить мои настройки по умолчанию':
        'Restaurar mis valores predeterminados',
    'Вернуть':
        'Restaurar',
    'Сохранить текущие как мои настройки по умолчанию':
        'Guardar los actuales como mis valores predeterminados',
    'Настройки лаунчера и bbport.ini, без назначений кнопок':
        'Ajustes del launcher y de bbport.ini, sin las asignaciones de botones',
    'Сохранить':
        'Guardar',
    'Из {}':
        'De {}',
    'Своих настроек по умолчанию пока нет: восстанавливаются встроенные (папки и ключ трофеев не меняются)':
        'Aún no tienes valores predeterminados propios: se restauran los integrados (las carpetas y la clave de trofeos se mantienen)',
    'Не удалось прочитать {}':
        'No se pudo leer {}',
    'Восстановить настройки по умолчанию?':
        '¿Restaurar los valores predeterminados?',
    'Настройки лаунчера и bbport.ini станут такими, как в {}. Остальные строки bbport.ini, в том числе назначения кнопок, не меняются':
        'Los ajustes del launcher y de bbport.ini pasan a ser los de {}. Las demás líneas de bbport.ini, incluidas las asignaciones de botones, no cambian',
    'Своих настроек по умолчанию нет: настройки лаунчера и bbport.ini станут встроенными. Папки, ключ трофеев и назначения кнопок не меняются':
        'No tienes valores predeterminados propios: los ajustes del launcher y de bbport.ini vuelven a los integrados. Las carpetas, la clave de trofeos y las asignaciones de botones no cambian',
    'Настройки по умолчанию восстановлены':
        'Valores predeterminados restaurados',
    'Сохранить текущие настройки как свои по умолчанию?':
        '¿Guardar los ajustes actuales como tus valores predeterminados?',
    'Они запишутся в {} вместо прежних, и «Вернуть» будет восстанавливать их':
        'Se escriben en {} en lugar de los anteriores, y «Restaurar» vuelve a ellos',
    'Не удалось сохранить {}':
        'No se pudo guardar {}',
    'Текущие настройки сохранены как ваши по умолчанию':
        'Ajustes actuales guardados como tus valores predeterminados',
    # Online page (LAN versus)
    "Версус по локальной сети: VS MODE в меню «Онлайн» игры, через ваш сервер shadNet (shadnet-p2p с патчем gzport). У каждого игрока своя учётная запись на этом сервере": "Versus por la red local: VS MODE en el menú «Online» del juego, a través de tu propio servidor shadNet (shadnet-p2p con el parche de gzport). Cada jugador tiene su propia cuenta en ese servidor",
    "Как настроить версус по сети": "Cómo configurar el versus en red",
    "Имя учётной записи на сервере shadNet (оно же ваше имя в игре) и её пароль. Пароль хранится на этом компьютере вместе с настройками лаунчера": "El nombre de tu cuenta en el servidor shadNet (también tu nombre en el juego) y su contraseña. La contraseña se guarda en este ordenador con los ajustes del lanzador",
    "Порт P2P (UDP)": "Puerto P2P (UDP)",
    "Через него игроки соединяются напрямую; он должен быть открыт между компьютерами": "Los jugadores se conectan directamente a través de él; debe estar abierto entre los ordenadores",
    "Укажите адрес сервера": "Introduce la dirección del servidor",
    "UDP сервера shadNet": "UDP del servidor shadNet",
    "отвечает; сервер видит этот компьютер как {}": "responde; el servidor ve este ordenador como {}",
    "не отвечает: матч не соединится": "no responde: la partida no se conectará",
}


# Italian.
IT = {
    "Папка DLC": "Cartella dei DLC",
    "Выбрать папку DLC": "Scegli la cartella dei DLC",
    "Не использовать DLC": "Non usare i DLC",
    "Найдено DLC: {}": "DLC trovati: {}",
    "Не используется": "Non usata",
    "Нет DLC этой игры в папке": "Nessun DLC di questo gioco nella cartella",
    "Запустить": "Gioca",
    "Остановить": "Ferma",
    "Настройки": "Impostazioni",
    "Журнал": "Log",
    "Не удалось запустить: {}": "Impossibile avviare: {}",
    "\n— игра завершилась (код {}) —\n": "\n— il gioco è terminato (codice {}) —\n",
    "Язык лаунчера": "Lingua del launcher",
    "Как в системе": "Sistema",
    "Применится после перезапуска лаунчера, пока игра запущена": "Si applica dopo il riavvio del launcher mentre il gioco è in esecuzione",
    "Игра": "Gioco",
    "Папка игры ({})": "Cartella del gioco ({})",
    "Папка игры": "Cartella del gioco",
    "Выбрать папку с eboot.bin": "Scegli la cartella con eboot.bin",
    "Открыть в файловом менеджере": "Apri nel gestore di file",
    "Папка сохранений": "Cartella dei salvataggi",
    "Выбрать папку сохранений": "Scegli la cartella dei salvataggi",
    "Вернуть папку по умолчанию": "Torna alla cartella predefinita",
    "Язык системы": "Lingua di sistema",
    "По умолчанию: {}": "Predefinito: {}",
    "Найдены сохранения": "Salvataggi trovati",
    "Сохранений пока нет: игра создаст их здесь": "Ancora nessun salvataggio: il gioco li creerà qui",
    "не выбрана": "non scelta",
    "Нет eboot.bin в папке": "Nessun eboot.bin nella cartella",
    "Управление": "Controlli",
    "Геймпад": "Gamepad",
    "Назначение кнопок; применяется при запуске игры": "Assegnazione dei tasti; si applica all'avvio del gioco",
    "Назначить": "Assegna",
    "Сбросить": "Ripristina",
    "{} (по умолчанию)": "{} (predefinito)",
    "не назначено": "non assegnato",
    "Нажмите клавишу или кнопку… (Esc — отмена)": "Premi un tasto o un pulsante… (Esc per annullare)",
    "Крест": "Croce",
    "Круг": "Cerchio",
    "Квадрат": "Quadrato",
    "Треугольник": "Triangolo",
    "Крестовина вверх": "Croce direzionale su",
    "Крестовина вниз": "Croce direzionale giù",
    "Крестовина влево": "Croce direzionale sinistra",
    "Крестовина вправо": "Croce direzionale destra",
    "Движение вперёд": "Muoviti avanti",
    "Движение назад": "Muoviti indietro",
    "Движение влево": "Muoviti a sinistra",
    "Движение вправо": "Muoviti a destra",
    "Камера вверх": "Camera su",
    "Камера вниз": "Camera giù",
    "Камера влево": "Camera a sinistra",
    "Камера вправо": "Camera a destra",
    "Контроллер": "Controller",
    "Выбранный берётся, как только подключится": "Quello scelto viene usato non appena si connette",
    "Первый подключённый": "Il primo connesso",
    "{} (не подключён)": "{} (non connesso)",
    "eboot.bin не читается как расшифрованный исполняемый файл PS4: сделайте дамп заново": "eboot.bin non può essere letto come eseguibile PS4 decriptato: estrai di nuovo il gioco",
    "Папка игры (с eboot.bin)": "Cartella del gioco (con eboot.bin)",
    "Английский": "Inglese",
    "Русский": "Russo",
    "Французский": "Francese",
    "Испанский": "Spagnolo",
    "Обновить список": "Aggiorna l'elenco",
    "Сторонние патчи": "Patch di terze parti",
    "Папка патчей": "Cartella delle patch",
    "Выбрать папку патчей": "Scegli la cartella delle patch",
    "Открыть папку патчей": "Apri la cartella delle patch",
    "Патчей нет": "Nessuna patch",
    "Автор: {}": "Autore: {}",
    "Экран": "Schermo",
    "Разрешение вывода": "Risoluzione di uscita",
    "Апскейлер дорисовывает кадр; Steam Deck — 720p": "L'upscaler riempie il fotogramma; Steam Deck: 720p",
    "Полноэкранный режим": "Schermo intero",
    "Смена разрешения на лету": "Cambio di risoluzione in tempo reale",
    "Без перезапуска, но медленнее на Steam Deck и старых GPU": "Non serve riavviare, ma è più lento su Steam Deck e GPU meno recenti",
    "Авто (по видеокарте)": "Auto (in base alla GPU)",
    "Выключена (быстрее)": "Disattivato (più veloce)",
    "Включена": "Attivato",
    "Режим показа кадров": "Modalità di presentazione",
    "Разрешить HDR": "Consenti HDR",
    "Апскейлер": "Upscaler",
    "Хранится в bbport.ini; в игре меняется через меню (Insert или L3+R3)": "Salvato in bbport.ini; in gioco, cambialo nel menu (Insert o L3+R3)",
    "TAA (нативное сглаживание)": "TAA (anti-aliasing nativo)",
    "Выключен": "Disattivato",
    "Пресет": "Preset",
    "Резкость (RCAS)": "Nitidezza (RCAS)",
    "Сила резкости": "Nitidezza",
    "Векторы движения объектов": "Vettori di movimento degli oggetti",
    "Меньше гостинга на персонажах; стоит около 10% FPS": "Meno ghosting sui personaggi; costa circa il 10% di FPS",
    "Показывать FPS": "Mostra FPS",
    "Ассеты найдены": "Risorse trovate",
    "Нет ассетов: tools/fetch_fsr4_assets.sh": "Nessuna risorsa: tools/fetch_fsr4_assets.sh",
    "Ассеты для выбранного режима найдены": "Risorse per la modalità selezionata trovate",
    "{}. Соберите FSR 4.1.1 из своей DLL кнопкой «Выбрать DLL…» ниже": "{}. Crea FSR 4.1.1 dalla tua DLL con il pulsante «Scegli DLL…» qui sotto",
    "FSR 4.1.1 из своей DLL AMD": "FSR 4.1.1 dalla tua DLL AMD",
    "Отменить": "Annulla",
    "Выбрать DLL…": "Scegli DLL…",
    "DLL апскейлера AMD (amd_fidelityfx_upscaler_dx12.dll)": "DLL dell'upscaler AMD (amd_fidelityfx_upscaler_dx12.dll)",
    "нет": "nessuno",
    "Эта DLL не подходит": "Questa DLL non è adatta",
    "{}: версия {}, модели FSR 4: {}.\n\nbbport повторяет только официальную FSR 4.1.x от AMD (модель v07_fp8_no_scale): например, FSR4_LATEST из OptiScaler или amd_fidelityfx_upscaler_dx12.dll из игры с FSR 4.1. Сборки сообщества (4.0.2b и подобные) устроены иначе и пока не поддерживаются.": "{}: versione {}, modelli FSR 4: {}.\n\nbbport riproduce solo l'FSR 4.1.x ufficiale di AMD (modello v07_fp8_no_scale): per esempio FSR4_LATEST di OptiScaler, oppure amd_fidelityfx_upscaler_dx12.dll di un gioco con FSR 4.1. Le build della community (4.0.2b e simili) hanno una struttura diversa e non sono ancora supportate.",
    "Загрузчик не подходит": "Il loader non è adatto",
    "Загрузчик FidelityFX (amd_fidelityfx_loader_dx12.dll или amd_fidelityfx_dx12.dll)": "Loader FidelityFX (amd_fidelityfx_loader_dx12.dll o amd_fidelityfx_dx12.dll)",
    "\n— сборка FSR 4.1.1 из {} —\n": "\n— creazione di FSR 4.1.1 da {} —\n",
    "Подготовка…": "Preparazione…",
    "Запись проходов DLL под Proton: {} из {}": "Registrazione dei passaggi della DLL con Proton: {} di {}",
    "Перевод проходов в SPIR-V…": "Traduzione dei passaggi in SPIR-V…",
    "— сборка FSR 4.1.1 завершилась (код {}) —\n": "— creazione di FSR 4.1.1 terminata (codice {}) —\n",
    "FSR 4.1.1 собран и выбран": "FSR 4.1.1 creato e selezionato",
    "Сборка FSR 4.1.1 отменена": "Creazione di FSR 4.1.1 annullata",
    "FSR 4.1.1 не собран": "FSR 4.1.1 non è stato creato",
    "DLL не подходит: подробности в журнале": "La DLL non è adatta: dettagli nel log",
    "Не хватает программ для сборки: список в журнале": "Mancano gli strumenti per la build: l'elenco è nel log",
    "Записанные проходы не совпали с тем, что повторяет bbport (другая версия DLL или новая видеокарта?): подробности в журнале": "I passaggi registrati non corrispondono a quelli che bbport riproduce (un'altra versione della DLL, o una nuova GPU?): dettagli nel log",
    "Не найден загрузчик FidelityFX 2.x": "Nessun loader FidelityFX 2.x trovato",
    "Не найден подходящий Proton: установите GE-Proton 10 или новее (ProtonUp-Qt) или Proton Experimental / Proton-CachyOS в Steam. Если они есть — запустите в Steam любую игру с этим Proton, чтобы Steam поставил его рантайм": "Nessun Proton adatto trovato: installa GE-Proton 10 o successivo (ProtonUp-Qt), oppure Proton Experimental / Proton-CachyOS in Steam. Se li hai, avvia un qualsiasi gioco con quel Proton in Steam, così che Steam installi il suo runtime",
    "Ни один Proton не запустил FSR 4.1 из этой DLL. Либо они слишком старые (подходят GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), либо DLL не включает FSR 4.1 на этой видеокарте (Steam Deck?): тогда соберите на ПК с Radeon RX 7000/9000 и скопируйте папку fsr4_411. Подробности в журнале": "Nessun Proton ha avviato l'FSR 4.1 di questa DLL. O sono troppo vecchi (funzionano GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), oppure la DLL non attiva FSR 4.1 su questa GPU (Steam Deck?): in tal caso crea la build su un PC con una Radeon RX 7000/9000 e copia la cartella fsr4_411. Dettagli nel log",
    "На NixOS запись идёт на самой системе (systemd --user) через umu-launcher из nix-shell, а здесь их не нашлось: установите umu-launcher или Nix. Подробности в журнале": "Su NixOS la registrazione viene eseguita sul sistema stesso (systemd --user) con umu-launcher da nix-shell, e nessuno dei due è stato trovato: installa umu-launcher o Nix. Dettagli nel log",
    "{}: FSR {}. Это официальная FSR 4.0.x от AMD: она включается только на видеокартах RDNA4 (RX 9000), а под Proton на других видеокартах не запускается, поэтому записать её нельзя.\n\nНужна FSR 4.1.x: например, FSR4_LATEST из OptiScaler или DLL из игры с FSR 4.1.": "{}: FSR {}. Questo è l'FSR 4.0.x ufficiale di AMD: è attivo solo sulle GPU RDNA4 (RX 9000) e su altre GPU non si avvia con Proton, quindi non può essere registrato.\n\nServe FSR 4.1.x: per esempio FSR4_LATEST di OptiScaler, o la DLL di un gioco con FSR 4.1.",
    "{}: в этой DLL нет FSR 4. Нужна amd_fidelityfx_upscaler_dx12.dll версии 4.1.x.": "{}: questa DLL non contiene FSR 4. Serve amd_fidelityfx_upscaler_dx12.dll versione 4.1.x.",
    "Это не загрузчик": "Questo non è il loader",
    "{} — это DLL апскейлера. Загрузчик называется amd_fidelityfx_loader_dx12.dll (у OptiScaler — amd_fidelityfx_dx12.dll) и лежит в той же папке игры, что и DLL апскейлера.": "{} è la DLL dell'upscaler. Il loader si chiama amd_fidelityfx_loader_dx12.dll (amd_fidelityfx_dx12.dll in OptiScaler) e si trova nella stessa cartella del gioco della DLL dell'upscaler.",
    "{}: версия {}. Нужен загрузчик FidelityFX 2.x — из той же игры, что и DLL апскейлера.": "{}: versione {}. Serve un loader FidelityFX 2.x, dello stesso gioco della DLL dell'upscaler.",
    "Рядом с DLL нет загрузчика: выберите amd_fidelityfx_loader_dx12.dll из папки игры": "Nessun loader accanto alla DLL: scegli amd_fidelityfx_loader_dx12.dll dalla cartella del gioco",
    "Собрать FSR 4.1.1 из amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: папка FSR4_LATEST, или из игры с FSR 4.1). Нужен GE-Proton 10+, Proton Experimental или Proton-CachyOS; 2–5 минут (RDNA4: вдвое дольше, ещё и вариант FP8)": "Crea FSR 4.1.1 da amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: la cartella FSR4_LATEST, oppure da un gioco con FSR 4.1). Richiede GE-Proton 10+, Proton Experimental o Proton-CachyOS; 2–5 minuti (RDNA4: il doppio, con la variante FP8)",
    "Сборка не удалась (код {}): подробности в журнале": "La build non è riuscita (codice {}): dettagli nel log",
    "Сглаживание в разрешении вывода без модели FSR": "Anti-aliasing alla risoluzione di uscita, senza modello FSR",
    "Нет или повреждён файл {}": "File {} mancante o danneggiato",
    "Пропуск заставок при запуске": "Salta i video introduttivi",
    "Частота кадров": "Frequenza dei fotogrammi",
    "Режим": "Modalità",
    "Какой патч частоты кадров применить к игре": "Quale patch della frequenza dei fotogrammi applicare al gioco",
    "Без ограничения (патч)": "Sbloccata (patch)",
    "60 (как на PS4)": "60 (come su PS4)",
    "Ограничение FPS": "Limite di FPS",
    "0 — без ограничения; укажите число, чтобы ограничить FPS": "0: nessun limite; imposta un numero per limitare la frequenza dei fotogrammi",
    "Производительность": "Prestazioni",
    "Двухстадийный конвейер GPU": "Pipeline GPU a due stadi",
    "Быстрее на 20–30%; при нестабильности выключите": "Più veloce del 20–30%; disattivala se è instabile",
    "Авто": "Auto",
    "Включён при 8 и более потоках процессора": "Attivata con 8 o più thread CPU",
    "Включён": "Attivata",
    "Стабильнее, но медленнее": "Più stabile, ma più lenta",
    "Чтение данных GPU процессором": "Letture dei dati della GPU da parte della CPU",
    "По умолчанию": "Predefinito",
    "Фоновая загрузка в видеопамять": "Precaricamento in background nella VRAM",
    "Меньше рывков при подгрузке зон": "Meno scatti quando le aree vengono caricate",
    "Обычная": "Normale",
    "Без лишней видеопамяти": "Nessuna VRAM extra",
    "Полная": "Completo",
    "Около 3 ГБ видеопамяти сверху": "Circa 3 GB di VRAM in più",
    "Режим работы": "Modalità",
    "Синхронизация как в 0.3": "Sincronizzazione come nella 0.3",
    "Для поиска регрессий: старая модель памяти и ожидания копий как в релизе 0.3": "Per trovare regressioni: il vecchio modello di memoria e le attese di copia come rilasciati nella 0.3",
    "Выключена": "Disattivata",
    "Выключены": "Disattivata",
    "Для разработчика": "Sviluppatore",
    "Статистика кадров в журнале": "Statistiche dei fotogrammi nel log",
    "Сохранять журнал и статистику в файл": "Salva il log e le statistiche in un file",
    "Диагностика вылетов": "Diagnostica dei crash",
    "Проверяет кучу игры и записывает записи в её память; немного медленнее": "Controlla l'heap del gioco e registra le scritture nella sua memoria; un po' più lento",
    "В папку logs в каталоге данных: для разбора рывков и вылетов": "Nella cartella logs della directory dei dati: per analizzare scatti e crash",
    "Профиль GPU в журнале": "Profilo GPU nel log",
    "Слои валидации Vulkan": "Layer di validazione Vulkan",
    "Сильно замедляет": "Molto più lento",
    "Доп. переменные (ИМЯ=значение через пробел)": "Variabili aggiuntive (NOME=valore, separate da spazi)",
    # Add to Steam
    "Добавить в Steam": "Aggiungi a Steam",
    "Игра в библиотеке Steam запускается сразу, с настройками этого лаунчера": "Dalla libreria di Steam il gioco si avvia subito, con le impostazioni di questo launcher",
    "Добавить": "Aggiungi",
    "Steam не найден (или в него ещё никто не входил)": "Steam non trovato (o nessuno vi ha ancora effettuato l'accesso)",
    "Закройте Steam и нажмите «Добавить» ещё раз": "Chiudi Steam e premi di nuovo Aggiungi",
    "Пока игра добавляется, Steam нужно закрыть; потом он запустится снова. Закрыть Steam?": "Steam deve chiudersi mentre il gioco viene aggiunto; poi si riavvia. Chiudere Steam?",
    "Отмена": "Annulla",
    "Закрыть Steam": "Chiudi Steam",
    "Steam не закрылся. Закройте его сами и попробуйте ещё раз": "Steam non si è chiuso. Chiudilo tu e riprova",
    "Не удалось добавить игру в Steam: {}": "Impossibile aggiungere il gioco a Steam: {}",
    # Online page
    "Онлайн": "Online",
    "Играть онлайн": "Gioca online",
    "Выключено: игра остаётся офлайн, как раньше": "Disattivato: il gioco resta offline, come prima",
    "Учётная запись": "Account",
    "Пароль": "Password",
    "Соединение": "Connessione",
    "Проверить соединение": "Prova la connessione",
    "Проверить": "Prova",
    "Сервер shadNet": "Server shadNet",
    "Проверка…": "Verifica…",
    "доступен": "raggiungibile",
    "недоступен": "non raggiungibile",
    # Button prompts
    "Применяется при запуске игры": "Si applica all'avvio del gioco",
    "Поменять местами A и B": "Scambia A e B",
    "Для контроллеров в стиле Nintendo: подтверждение на A, отмена на B. Применяется при запуске игры": "Per controller in stile Nintendo: conferma con A, indietro con B. Si applica all'avvio del gioco",
    "Поменять стики местами": "Scambiare gli stick",
    "Инвертировать камеру геймпада по горизонтали": "Invertire la telecamera del controller in orizzontale",
    "Инвертировать камеру геймпада по вертикали": "Invertire la telecamera del controller in verticale",
    "Импортировать сохранения…": "Importa salvataggi…",
    "Импорт сохранений": "Importa salvataggi",
    "Это копия с PS4 на флешке (sdimg_*): она зашифрована ключами консоли. Экспортируйте сохранение без шифрования на PS4 (Apollo Save Tool) или через Save Wizard": "È una copia della PS4 per chiavetta USB (sdimg_*): è cifrata con le chiavi della console. Esporta il salvataggio non cifrato sulla PS4 (Apollo Save Tool) o con Save Wizard",
    "Импортировать сохранения?": "Importare i salvataggi?",
    "Из {} (изменены {}). Текущие сохранения сначала копируются в {}": "Da {} (modificati il {}). I salvataggi attuali vengono prima copiati in {}",
    "Импортировать": "Importa",
    "Не удалось импортировать сохранения": "Impossibile importare i salvataggi",
    "Сохранения импортированы": "Salvataggi importati",
    # Add to Steam with Flathub's Steam
    'Steam из Flatpak запускает игры в своей песочнице, где нет ни папки игры, ни драйверов: ярлык должен запускать игру вне её (flatpak-spawn --host). Для этого Steam нужно право org.freedesktop.Flatpak, с которым он может запускать программы в вашей системе. Выдать его?':
        'Steam da Flatpak avvia i giochi nella sua sandbox, dove non ci sono né la cartella del gioco né i driver: il collegamento deve avviare il gioco fuori da essa (flatpak-spawn --host). Per questo Steam ha bisogno del permesso org.freedesktop.Flatpak, che gli consente di avviare programmi sul tuo sistema. Concederlo?',
    'Выдать право':
        'Concedi il permesso',
    'Не удалось выдать право Steam: {}':
        'Impossibile concedere il permesso a Steam: {}',
    "Копировать":
        "Copia",
    "Экспорт журнала…":
        "Esporta registro…",
    "Экспорт журнала":
        "Esporta registro",
    "Журнал скопирован":
        "Registro copiato",
    "Журнал сохранён: {}":
        "Registro salvato: {}",
    "Не удалось сохранить журнал: {}":
        "Impossibile salvare il registro: {}",
    "Монитор":
        "Monitor",
    "Основной":
        "Principale",
    ", основной":
        ", principale",
    "Новая: видеокарта работает с памятью игры напрямую, как в игре для ПК, а команды графики переводятся, а не эмулируются. Старая — модель памяти 0.3 со всеми исправлениями. Если драйвер не проходит проверку при запуске — старая":
        "Il nuovo: la scheda video lavora direttamente con la memoria del gioco, come in un gioco per PC, e i comandi grafici vengono tradotti invece che emulati. Il vecchio: il modello di memoria della 0.3 con tutte le correzioni. Se il driver non supera il controllo all'avvio, il vecchio",
    "Модель памяти и трансляции":
        "Modello di memoria e traduzione",
    "Авто: новая на AMD, старая на других":
        "Automatico: nuovo su AMD, vecchio sulle altre",
    "Новая":
        "Nuovo",
    "Старая (как в 0.3)":
        "Vecchio (come nella 0.3)",
    "О программе":
        "Informazioni",
    "Сначала закройте игру":
        "Chiudi prima il gioco",
    "Основано на bbport от deadinside28":
        "Basato su bbport di deadinside28",
    "Лицензия":
        "Licenza",
    'GNU GPL v2 или новее · Файлы игры не входят.': 'GNU GPL v2 o successiva · Nessun file del gioco incluso.',
    # 0.51: mouse look, choosing NVIDIA's DLSS library, the online module
    'DLSS {}: готово':
        'DLSS {}: pronto',
    'DLSS найден (нужна видеокарта NVIDIA RTX)':
        'DLSS trovato (serve una GPU NVIDIA RTX)',
    'DLSS не найден: выберите библиотеку NVIDIA ниже (и нужна сборка с мостом DLSS). Игра включит FSR 3.1':
        'DLSS non trovato: scegli la libreria NVIDIA qui sotto (serve anche una build con il bridge DLSS). Il gioco userà FSR 3.1',
    'DLSS: библиотека NVIDIA':
        'DLSS: libreria NVIDIA',
    '{} — библиотека DLSS для Windows; на Linux NVIDIA её не загружает. Нужна libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        '{} è la libreria DLSS per Windows; il driver NVIDIA per Linux non la carica. Serve libnvidia-ngx-dlss.so.<versione> dal DLSS SDK di NVIDIA: {}',
    'Библиотека DLSS NVIDIA (libnvidia-ngx-dlss.so.*)':
        'Libreria DLSS di NVIDIA (libnvidia-ngx-dlss.so.*)',
    'Выбрать файл…':
        'Scegli file…',
    'Из сборки: {}':
        'Da questa build: {}',
    'Инвертировать мышь по вертикали':
        "Inverti l'asse Y del mouse",
    'Камера мышью':
        'Visuale con il mouse',
    'Клавиатура и мышь':
        'Tastiera e mouse',
    'Не удалось прочитать файл':
        'Impossibile leggere il file',
    'Не удалось скопировать библиотеку':
        'Impossibile copiare la libreria',
    'Нет: выберите libnvidia-ngx-dlss.so.* из DLSS SDK NVIDIA ({})':
        'Nessuna: scegli libnvidia-ngx-dlss.so.* dal DLSS SDK di NVIDIA ({})',
    'Нужен файл libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        'Serve libnvidia-ngx-dlss.so.<versione> dal DLSS SDK di NVIDIA: {}',
    'Нужна библиотека для Linux':
        'Serve una libreria per Linux',
    'Своя: {}':
        'La tua: {}',
    'Убрать выбранную':
        'Rimuovi quella scelta',
    'Чувствительность мыши':
        'Sensibilità del mouse',
    'Щелчок в окне игры захватывает мышь, F1 — отпускает':
        'Un clic nella finestra del gioco cattura il mouse, F1 lo rilascia',
    'Эта сборка без модуля онлайна (libbbnet.so): игра только офлайн':
        'Questa build non ha il modulo online (libbbnet.so): solo gioco offline',
    'Эта сборка без моста DLSS (libbbport_dlss.so): DLSS работать не будет':
        'Questa build non ha il bridge DLSS (libbbport_dlss.so): DLSS non funzionerà',
    'Это не библиотека DLSS':
        'Non è la libreria DLSS',
    # Online page: the server
    'Адрес сервера (host:port)':
        'Indirizzo del server (host:porta)',
    'Сервер shadNet':
        'Server shadNet',
    # Trophies page
    'В дампе игры нет трофеев (sce_sys/trophy)':
        'Il dump del gioco non ha trofei (sce_sys/trophy)',
    'Записываются, когда игра их открывает, и показываются в игре':
        'Registrati quando il gioco li sblocca, e mostrati nel gioco',
    'Ключ трофеев':
        'Chiave dei trofei',
    'Неверный ключ трофеев: названия недоступны':
        'Chiave dei trofei errata: i nomi non sono disponibili',
    'Получен {}':
        'Ottenuto il {}',
    'Получено {} из {}':
        '{} di {} ottenuti',
    'Скрытый трофей':
        'Trofeo nascosto',
    'Трофеи':
        'Trofei',
    'Платиновый':
        'Platino',
    'Золотой':
        'Oro',
    'Серебряный':
        'Argento',
    'Бронзовый':
        'Bronzo',
    "Вход в shadNet": "Accesso a shadNet",
    "неверное имя или пароль": "nome o password errati",
    "такой учётной записи нет на этом сервере": "questo account non esiste su questo server",
    "эта учётная запись уже в сети (игра запущена?)": "questo account ha già effettuato l'accesso (il gioco è aperto?)",
    "вход выполнен": "accesso riuscito",
    "вход не удался ({})": "accesso non riuscito ({})",
    # About: Thanks
    'Благодарности': 'Ringraziamenti',
    'Без них ничего этого не было бы': 'Senza di loro, niente di tutto questo sarebbe possibile',
    'Порт и его код': 'Il port e il suo codice',
    'Помощь и тесты': 'Aiuto e test',
    'Другие благодарности': 'Grazie anche a',
    'bbport — порт, на котором построен весь этот проект': 'bbport, il port su cui si basa tutto questo progetto',
    'Игра по сети, DLSS, страница читов, добавление в Steam, значок, пропуск конвейеров, которые драйвер не может создать, и игра без вылета при нехватке видеопамяти': 'Gioco online, DLSS, la pagina dei trucchi, Aggiungi a Steam, l’icona, saltare le pipeline che il driver non riesce a creare e nessun crash quando finisce la memoria video',
    'Собрал и адаптировал десятки исправлений: вылеты при загрузке, чёрные изображения, апскейлер, строка производительности в журнале': 'Ha raccolto e adattato decine di correzioni: crash durante il caricamento, immagini nere, l’upscaler, la riga delle prestazioni nel log',
    'Чёрный предпросмотр персонажа, картинка экрана загрузки и память кэша текстур': 'L’anteprima nera del personaggio, l’immagine della schermata di caricamento e la memoria della cache delle texture',
    'Кэш текстур вовремя освобождает видеопамять': 'La cache delle texture libera la memoria video in tempo',
    'Вылеты при загрузке областей': 'Crash durante il caricamento delle aree',
    'Интерфейс, пропадавший не в 1080p, векторы движения больших чудовищ и ошибка памяти': 'L’interfaccia che spariva fuori da 1080p, i vettori di movimento delle grandi bestie e un errore di memoria',
    'Вылеты при загрузке некоторых карт и меню жестов с клавиатуры': 'Crash al caricamento di alcune mappe e il menu dei gesti da tastiera',
    'Экранная клавиатура для имени персонажа и уведомление о компиляции шейдеров': 'La tastiera su schermo per il nome del personaggio e l’avviso di compilazione degli shader',
    'Сетевые библиотеки игры по сети и сервер для своего кооператива': 'Le librerie del gioco online e il server per la propria cooperativa',
    'Основа поддержки DLSS и модель FSR 4 без шлейфов за персонажами': 'La base del supporto DLSS e il modello FSR 4 senza scie dietro i personaggi',
    'Апскейлер FSR 3.1': 'L’upscaler FSR 3.1',
    'Игра запускается, когда DLSS нельзя использовать': 'Il gioco si avvia quando DLSS non può essere usato',
    'Перевод на упрощённый китайский': 'La traduzione in cinese semplificato',
    'Звук игры на полной громкости': 'L’audio del gioco a pieno volume',
    'Флажки и ползунки внутриигрового меню': 'Le caselle e i cursori del menu di gioco',
    'Подробные отчёты с журналами и проверка исправлений': 'Segnalazioni dettagliate con log e test delle correzioni',
    'Идея поменять местами A и B на контроллерах в стиле Nintendo': 'L’idea di scambiare A e B sui controller in stile Nintendo',
    'Проверка исправления видеопамяти': 'Test della correzione della memoria video',
    'Рендерер и компилятор шейдеров': 'Il renderer e il ricompilatore degli shader',
    'Инструмент для сборки AppImage': 'Lo strumento che crea l’AppImage',
    'Нашёл ошибку, из-за которой игра не запускалась на некоторых видеокартах, и ускорение камеры на DualShock 4': 'Ha trovato il bug che impediva l’avvio del gioco su alcune schede video, e l’accelerazione della telecamera sul DualShock 4',
    'Нашёл, почему игра не запускалась в игровом режиме Steam Deck': 'Ha scoperto perché il gioco non si avviava nella modalità gioco di Steam Deck',
    'Нашёл, при каких эффектах зависают загрузки на NVIDIA': 'Ha scoperto quali effetti bloccano i caricamenti su NVIDIA',
    'ps4-pkg-extractor: установка игры из файлов .pkg': 'ps4-pkg-extractor: installare il gioco dai file .pkg',
    # Shader cache
    'Кэш шейдеров': 'Cache degli shader',
    'Очистить': 'Svuota',
    '{}. Если после обновления картинка выглядит странно, очистите его: шейдеры соберутся заново (первые минуты в каждой зоне возможны рывки)': '{}. Se l’immagine sembra strana dopo un aggiornamento, svuotala: gli shader vengono ricreati (possibili scatti nei primi minuti di ogni area)',
    'Пусто: шейдеры соберутся при игре': 'Vuota: gli shader vengono creati mentre giochi',
    'Очистить кэш шейдеров?': 'Svuotare la cache degli shader?',
    'Игра соберёт шейдеры заново: первые минуты в каждой зоне возможны рывки. Сохранения и настройки не затрагиваются.': 'Il gioco ricrea gli shader: possibili scatti nei primi minuti di ogni area. Salvataggi e impostazioni non vengono toccati.',
    'Названия трофеев на английском без ключа и звук при получении трофея': 'I nomi dei trofei in inglese senza la chiave e il suono quando se ne ottiene uno',
    'Буфер трафарета, в который писали цветные изображения': 'Lo stencil buffer in cui scrivevano immagini a colori',
    'Вход на публичный сервер shadNet без отключения': 'Restare connessi al server pubblico di shadNet',
    'Установить из PKG': 'Installa da PKG',
    'Выбрать .pkg…': 'Scegli .pkg…',
    'Файлы .pkg: игра, обновление, DLC': 'File .pkg: gioco, aggiornamento, DLC',
    'Куда установить игру': 'Dove installare il gioco',
    'Установка…': 'Installazione…',
    'Игра установлена: {}': 'Gioco installato: {}',
    'Не удалось установить: подробности в журнале': 'Impossibile installare: dettagli nel registro',
    'Выход из игры из меню с контроллера, меню в пределах экрана и половины тачпада на Xbox': 'Uscire dal gioco dal menu con il controller, il menu entro lo schermo e le metà del touchpad sui controller Xbox',
    'Вылет видеоплеера при его остановке': 'Un crash del lettore video quando si ferma',
    'Язык внутриигрового меню при запуске без окна лаунчера': 'La lingua del menu di gioco avviando senza la finestra del launcher',
    'DLSS в AppImage на NVIDIA': "DLSS nell'AppImage su NVIDIA",
    'Сверхширокие мониторы без растянутой картинки': 'Monitor ultrawide senza immagine stirata',
    'Движение с клавиатуры: круглая диагональ и последняя нажатая клавиша': 'Movimento da tastiera: diagonale rotonda e l’ultimo tasto premuto',
    'Отладка вылетов: процесс ждёт отладчик (BB_FAULT_WAIT)': 'Debug dei crash: il processo attende un debugger (BB_FAULT_WAIT)',
    'Видеопамять на картах с 4 ГБ и вылеты: флипы, swapchain, дескрипторы и ошибки страниц; смена стиков и инверсия камеры, импорт сохранений, выбор версии': 'Memoria video su schede da 4 GB e crash: flip, swapchain, descrittori ed errori di pagina; scambio degli stick e inversione della telecamera, importazione dei salvataggi, selettore di versione',
    'Большие группы команд записи и swapchain после изменений экрана': 'Grandi gruppi di comandi registrati e la swapchain dopo i cambi di schermo',
    # GODZILLA (gzport)
    'GODZILLA {}, версия 1.01':
        'GODZILLA {}, versione 1.01',
    'GODZILLA добавлена в библиотеку Steam':
        'GODZILLA aggiunto alla libreria di Steam',
    'GODZILLA — товарный знак Toho Co., Ltd.; игра для PS4 издана Bandai Namco Entertainment. Этот проект с ними не связан.':
        'GODZILLA è un marchio di Toho Co., Ltd.; il gioco per PS4 è stato pubblicato da Bandai Namco Entertainment. Questo progetto non è affiliato con loro.',
    'XML-патчи в формате shadPS4 для версии 01.01 из папки патчей. Применяются при запуске.':
        "Patch XML in formato shadPS4 per la versione 01.01 dalla cartella delle patch. Si applicano all'avvio.",
    'eboot.bin не от версии 1.01: скопируйте eboot.bin из дампа обновления 1.01 в папку игры с заменой':
        "eboot.bin non è della 1.01: copia eboot.bin dall'aggiornamento 1.01 estratto nella cartella del gioco, sostituendolo",
    'gzport — нативный порт для Linux':
        'gzport — port nativo per Linux',
    'Авторы bbport и bloodborne_linux, на которых построен gzport, и все, кто им помогал':
        'Gli autori di bbport e bloodborne_linux, su cui è costruito gzport, e tutti quelli che li hanno aiutati',
    'В папке игры нет: {}. Распакуйте игру и обновление 1.01 заново':
        'Mancano nella cartella del gioco: {}. Estrai di nuovo il gioco e l’aggiornamento 1.01',
    'В этой папке нет сохранений GODZILLA (SAVEDATA00 с DATA.BIN)':
        'Nessun salvataggio di GODZILLA in questa cartella (SAVEDATA00 con DATA.BIN)',
    'Игра идёт с 60 FPS, как на PS4. Выше 60 FPS: нужен патч частоты кадров, его пока нет':
        'Il gioco gira a 60 FPS, come su PS4. Oltre i 60 FPS serve una patch del frame rate, non ancora disponibile',
    'Для GODZILLA пока недоступен: игра рисует кадр прямо в разрешении вывода':
        'Non ancora disponibile per GODZILLA: il gioco disegna il fotogramma direttamente alla risoluzione d\'uscita',
    'Игра, обновление 1.01 и DLC из ваших файлов .pkg':
        'Il gioco, l’aggiornamento 1.01 e i DLC dai tuoi file .pkg',
    'Ключ трофеев PS4 (TrophyKey в shadPS4), 32 шестнадцатеричных символа: с ним названия и описания на языке игры. Хранится на этом компьютере. Без него видны только значки':
        'La chiave dei trofei PS4 (TrophyKey in shadPS4), 32 cifre esadecimali: con essa nomi e descrizioni sono nella lingua del gioco. Resta su questo computer. Senza, si vedono solo le icone',
    'Нативный порт для Linux, версия {}':
        'Port nativo per Linux, versione {}',
    'Нужен патч для версии 1.01, его пока нет':
        'Richiede una patch per la versione 1.01, non ancora disponibile',
    'Нужно обновление 1.01: скопируйте файлы дампа обновления 1.01 в папку игры с заменой (найдена версия {})':
        "Serve l'aggiornamento 1.01: copia l'aggiornamento 1.01 estratto nella cartella del gioco, sostituendo i file (versione trovata {})",
    'Основано на bloodborne_linux от ayozetr':
        'Basato su bloodborne_linux di ayozetr',
    'bloodborne_linux: порт для Linux, на котором построен gzport':
        'bloodborne_linux: il port per Linux su cui è costruito gzport',
    'Папка с сохранениями GODZILLA':
        'Cartella con i salvataggi di GODZILLA',
    'Патчи игры':
        'Patch del gioco',
    'Португальский (Бразилия)':
        'Portoghese (Brasile)',
    'Это не GODZILLA (найдено {}): нужна GODZILLA (CUSA02046) с обновлением 1.01':
        'Questo non è GODZILLA (trovato {}): serve GODZILLA (CUSA02046) con l’aggiornamento 1.01',
    'Тачпад, левая половина':
        'Touchpad, metà sinistra',
    'Тачпад, правая половина':
        'Touchpad, metà destra',
    'Настройки по умолчанию':
        'Predefiniti',
    'Восстановить мои настройки по умолчанию':
        'Ripristina i miei predefiniti',
    'Вернуть':
        'Ripristina',
    'Сохранить текущие как мои настройки по умолчанию':
        'Salva le attuali come miei predefiniti',
    'Настройки лаунчера и bbport.ini, без назначений кнопок':
        'Impostazioni del launcher e di bbport.ini, senza le assegnazioni dei tasti',
    'Сохранить':
        'Salva',
    'Из {}':
        'Da {}',
    'Своих настроек по умолчанию пока нет: восстанавливаются встроенные (папки и ключ трофеев не меняются)':
        'Non hai ancora predefiniti tuoi: vengono ripristinati quelli integrati (le cartelle e la chiave dei trofei restano)',
    'Не удалось прочитать {}':
        'Impossibile leggere {}',
    'Восстановить настройки по умолчанию?':
        'Ripristinare i predefiniti?',
    'Настройки лаунчера и bbport.ini станут такими, как в {}. Остальные строки bbport.ini, в том числе назначения кнопок, не меняются':
        'Le impostazioni del launcher e di bbport.ini diventano quelle di {}. Le altre righe di bbport.ini, comprese le assegnazioni dei tasti, non cambiano',
    'Своих настроек по умолчанию нет: настройки лаунчера и bbport.ini станут встроенными. Папки, ключ трофеев и назначения кнопок не меняются':
        'Non hai predefiniti tuoi: le impostazioni del launcher e di bbport.ini tornano a quelle integrate. Le cartelle, la chiave dei trofei e le assegnazioni dei tasti non cambiano',
    'Настройки по умолчанию восстановлены':
        'Predefiniti ripristinati',
    'Сохранить текущие настройки как свои по умолчанию?':
        'Salvare le impostazioni attuali come tuoi predefiniti?',
    'Они запишутся в {} вместо прежних, и «Вернуть» будет восстанавливать их':
        'Vengono scritte in {} al posto delle precedenti, e «Ripristina» le riporta',
    'Не удалось сохранить {}':
        'Impossibile salvare {}',
    'Текущие настройки сохранены как ваши по умолчанию':
        'Impostazioni attuali salvate come tuoi predefiniti',
    # Online page (LAN versus)
    "Версус по локальной сети: VS MODE в меню «Онлайн» игры, через ваш сервер shadNet (shadnet-p2p с патчем gzport). У каждого игрока своя учётная запись на этом сервере": "Versus sulla rete locale: VS MODE nel menu «Online» del gioco, tramite il tuo server shadNet (shadnet-p2p con la patch di gzport). Ogni giocatore ha un proprio account su quel server",
    "Как настроить версус по сети": "Come configurare il versus in rete",
    "Имя учётной записи на сервере shadNet (оно же ваше имя в игре) и её пароль. Пароль хранится на этом компьютере вместе с настройками лаунчера": "Il nome del tuo account sul server shadNet (anche il tuo nome nel gioco) e la sua password. La password è salvata su questo computer con le impostazioni del launcher",
    "Порт P2P (UDP)": "Porta P2P (UDP)",
    "Через него игроки соединяются напрямую; он должен быть открыт между компьютерами": "I giocatori si collegano direttamente attraverso di essa; deve essere aperta tra i computer",
    "Укажите адрес сервера": "Inserisci l'indirizzo del server",
    "UDP сервера shadNet": "UDP del server shadNet",
    "отвечает; сервер видит этот компьютер как {}": "risponde; il server vede questo computer come {}",
    "не отвечает: матч не соединится": "nessuna risposta: la partita non si collegherà",
}


# French.
FR = {
    "Папка DLC": "Dossier des DLC",
    "Выбрать папку DLC": "Choisir le dossier des DLC",
    "Не использовать DLC": "Ne pas utiliser de DLC",
    "Найдено DLC: {}": "DLC trouvés : {}",
    "Не используется": "Non utilisé",
    "Нет DLC этой игры в папке": "Aucun DLC de ce jeu dans le dossier",
    "Запустить": "Jouer",
    "Остановить": "Arrêter",
    "Настройки": "Paramètres",
    "Журнал": "Journal",
    "Не удалось запустить: {}": "Impossible de lancer : {}",
    "\n— игра завершилась (код {}) —\n": "\n— le jeu s'est arrêté (code {}) —\n",
    "Язык лаунчера": "Langue du lanceur",
    "Как в системе": "Système",
    "Применится после перезапуска лаунчера, пока игра запущена": "S'applique après le redémarrage du lanceur lorsque le jeu est en cours d'exécution",
    "Игра": "Jeu",
    "Папка игры ({})": "Dossier du jeu ({})",
    "Папка игры": "Dossier du jeu",
    "Выбрать папку с eboot.bin": "Choisissez le dossier contenant eboot.bin",
    "Открыть в файловом менеджере": "Ouvrir dans le gestionnaire de fichiers",
    "Папка сохранений": "Dossier des sauvegardes",
    "Выбрать папку сохранений": "Choisissez le dossier des sauvegardes",
    "Вернуть папку по умолчанию": "Revenir au dossier par défaut",
    "Язык системы": "Langue du système",
    "По умолчанию: {}": "Par défaut : {}",
    "Найдены сохранения": "Sauvegardes trouvées",
    "Сохранений пока нет: игра создаст их здесь": "Aucune sauvegarde pour l'instant : le jeu les créera ici",
    "не выбрана": "non choisi",
    "Нет eboot.bin в папке": "Pas de eboot.bin dans le dossier",
    "Управление": "Commandes",
    "Геймпад": "Manette",
    "Назначение кнопок; применяется при запуске игры": "Affectation des boutons ; appliquée au lancement du jeu",
    "Назначить": "Assigner",
    "Сбросить": "Réinitialiser",
    "{} (по умолчанию)": "{} (par défaut)",
    "не назначено": "non assigné",
    "Нажмите клавишу или кнопку… (Esc — отмена)": "Appuyez sur une touche ou un bouton… (Échap pour annuler)",
    "Крест": "Croix",
    "Круг": "Rond",
    "Квадрат": "Carré",
    "Треугольник": "Triangle",
    "Крестовина вверх": "Croix directionnelle haut",
    "Крестовина вниз": "Croix directionnelle bas",
    "Крестовина влево": "Croix directionnelle gauche",
    "Крестовина вправо": "Croix directionnelle droite",
    "Движение вперёд": "Avancer",
    "Движение назад": "Reculer",
    "Движение влево": "Aller à gauche",
    "Движение вправо": "Aller à droite",
    "Камера вверх": "Caméra vers le haut",
    "Камера вниз": "Caméra vers le bas",
    "Камера влево": "Caméra vers la gauche",
    "Камера вправо": "Caméra vers la droite",
    "Контроллер": "Manette",
    "Выбранный берётся, как только подключится": "Celle choisie est utilisée dès qu'elle se connecte",
    "Первый подключённый": "Première connectée",
    "{} (не подключён)": "{} (non connectée)",
    "eboot.bin не читается как расшифрованный исполняемый файл PS4: сделайте дамп заново": "eboot.bin ne peut pas être lu comme un exécutable PS4 déchiffré : extrayez de nouveau le jeu",
    "Папка игры (с eboot.bin)": "Dossier du jeu (avec eboot.bin)",
    "Английский": "Anglais",
    "Русский": "Russe",
    "Французский": "Français",
    "Испанский": "Espagnol",
    "Обновить список": "Actualiser la liste",
    "Сторонние патчи": "Correctifs tiers",
    "Папка патчей": "Dossier des correctifs",
    "Выбрать папку патчей": "Choisissez le dossier des correctifs",
    "Открыть папку патчей": "Ouvrir le dossier des correctifs",
    "Патчей нет": "Aucun correctif",
    "Автор: {}": "Auteur : {}",
    "Экран": "Affichage",
    "Разрешение вывода": "Résolution de sortie",
    "Апскейлер дорисовывает кадр; Steam Deck — 720p": "L'upscaler remplit l'image ; Steam Deck : 720p",
    "Полноэкранный режим": "Plein écran",
    "Смена разрешения на лету": "Changement de résolution en direct",
    "Без перезапуска, но медленнее на Steam Deck и старых GPU": "Aucun redémarrage nécessaire, mais plus lent sur le Steam Deck et les GPU plus anciens",
    "Авто (по видеокарте)": "Auto (selon le GPU)",
    "Выключена (быстрее)": "Désactivé (plus rapide)",
    "Включена": "Activé",
    "Режим показа кадров": "Mode de présentation",
    "Разрешить HDR": "Autoriser le HDR",
    "Апскейлер": "Upscaler",
    "Хранится в bbport.ini; в игре меняется через меню (Insert или L3+R3)": "Enregistré dans bbport.ini ; en jeu, modifiez-le dans le menu (Insert ou L3+R3)",
    "TAA (нативное сглаживание)": "TAA (anticrénelage natif)",
    "Выключен": "Désactivé",
    "Пресет": "Préréglage",
    "Резкость (RCAS)": "Netteté (RCAS)",
    "Сила резкости": "Netteté",
    "Векторы движения объектов": "Vecteurs de mouvement des objets",
    "Меньше гостинга на персонажах; стоит около 10% FPS": "Moins de ghosting sur les personnages ; coûte environ 10 % de FPS",
    "Показывать FPS": "Afficher les FPS",
    "Ассеты найдены": "Ressources trouvées",
    "Нет ассетов: tools/fetch_fsr4_assets.sh": "Pas de ressources : tools/fetch_fsr4_assets.sh",
    "Ассеты для выбранного режима найдены": "Ressources du mode sélectionné trouvées",
    "{}. Соберите FSR 4.1.1 из своей DLL кнопкой «Выбрать DLL…» ниже": "{}. Générez FSR 4.1.1 à partir de votre propre DLL avec le bouton « Choisir la DLL… » ci-dessous",
    "FSR 4.1.1 из своей DLL AMD": "FSR 4.1.1 à partir de votre propre DLL AMD",
    "Отменить": "Annuler",
    "Выбрать DLL…": "Choisir la DLL…",
    "DLL апскейлера AMD (amd_fidelityfx_upscaler_dx12.dll)": "DLL de l'upscaler AMD (amd_fidelityfx_upscaler_dx12.dll)",
    "нет": "aucun",
    "Эта DLL не подходит": "Cette DLL ne convient pas",
    "{}: версия {}, модели FSR 4: {}.\n\nbbport повторяет только официальную FSR 4.1.x от AMD (модель v07_fp8_no_scale): например, FSR4_LATEST из OptiScaler или amd_fidelityfx_upscaler_dx12.dll из игры с FSR 4.1. Сборки сообщества (4.0.2b и подобные) устроены иначе и пока не поддерживаются.": "{} : version {}, modèles FSR 4 : {}.\n\nbbport ne rejoue que le FSR 4.1.x officiel d'AMD (modèle v07_fp8_no_scale) : par exemple FSR4_LATEST d'OptiScaler, ou amd_fidelityfx_upscaler_dx12.dll d'un jeu avec FSR 4.1. Les builds communautaires (4.0.2b et similaires) ont une structure différente et ne sont pas encore pris en charge.",
    "Загрузчик не подходит": "Le loader ne convient pas",
    "Загрузчик FidelityFX (amd_fidelityfx_loader_dx12.dll или amd_fidelityfx_dx12.dll)": "Loader FidelityFX (amd_fidelityfx_loader_dx12.dll ou amd_fidelityfx_dx12.dll)",
    "\n— сборка FSR 4.1.1 из {} —\n": "\n— génération de FSR 4.1.1 à partir de {} —\n",
    "Подготовка…": "Préparation…",
    "Запись проходов DLL под Proton: {} из {}": "Enregistrement des passes de la DLL sous Proton : {} sur {}",
    "Перевод проходов в SPIR-V…": "Traduction des passes en SPIR-V…",
    "— сборка FSR 4.1.1 завершилась (код {}) —\n": "— génération de FSR 4.1.1 terminée (code {}) —\n",
    "FSR 4.1.1 собран и выбран": "FSR 4.1.1 généré et sélectionné",
    "Сборка FSR 4.1.1 отменена": "Génération de FSR 4.1.1 annulée",
    "FSR 4.1.1 не собран": "FSR 4.1.1 n'a pas été généré",
    "DLL не подходит: подробности в журнале": "La DLL ne convient pas : détails dans le journal",
    "Не хватает программ для сборки: список в журнале": "Des outils nécessaires à la génération sont manquants : la liste est dans le journal",
    "Записанные проходы не совпали с тем, что повторяет bbport (другая версия DLL или новая видеокарта?): подробности в журнале": "Les passes enregistrées ne correspondent pas à ce que bbport rejoue (autre version de la DLL, ou nouveau GPU ?) : détails dans le journal",
    "Не найден загрузчик FidelityFX 2.x": "Aucun loader FidelityFX 2.x trouvé",
    "Не найден подходящий Proton: установите GE-Proton 10 или новее (ProtonUp-Qt) или Proton Experimental / Proton-CachyOS в Steam. Если они есть — запустите в Steam любую игру с этим Proton, чтобы Steam поставил его рантайм": "Aucun Proton adapté trouvé : installez GE-Proton 10 ou plus récent (ProtonUp-Qt), ou Proton Experimental / Proton-CachyOS dans Steam. Si vous les avez, lancez n'importe quel jeu avec ce Proton dans Steam afin que Steam installe son runtime",
    "Ни один Proton не запустил FSR 4.1 из этой DLL. Либо они слишком старые (подходят GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), либо DLL не включает FSR 4.1 на этой видеокарте (Steam Deck?): тогда соберите на ПК с Radeon RX 7000/9000 и скопируйте папку fsr4_411. Подробности в журнале": "Aucun Proton n'a lancé le FSR 4.1 de cette DLL. Soit ils sont trop anciens (GE-Proton 10+, Proton Experimental, Proton-CachyOS 11 fonctionnent), soit la DLL n'active pas FSR 4.1 sur ce GPU (Steam Deck ?) : dans ce cas, faites la génération sur un PC avec une Radeon RX 7000/9000 et copiez le dossier fsr4_411. Détails dans le journal",
    "На NixOS запись идёт на самой системе (systemd --user) через umu-launcher из nix-shell, а здесь их не нашлось: установите umu-launcher или Nix. Подробности в журнале": "Sous NixOS, l'enregistrement s'exécute sur le système lui-même (systemd --user) avec umu-launcher depuis nix-shell, et aucun des deux n'a été trouvé : installez umu-launcher ou Nix. Détails dans le journal",
    "{}: FSR {}. Это официальная FSR 4.0.x от AMD: она включается только на видеокартах RDNA4 (RX 9000), а под Proton на других видеокартах не запускается, поэтому записать её нельзя.\n\nНужна FSR 4.1.x: например, FSR4_LATEST из OptiScaler или DLL из игры с FSR 4.1.": "{} : FSR {}. Il s'agit du FSR 4.0.x officiel d'AMD : il n'est activé que sur les GPU RDNA4 (RX 9000) et ne démarre pas sous Proton sur les autres GPU, il ne peut donc pas être enregistré.\n\nFSR 4.1.x est nécessaire : par exemple FSR4_LATEST d'OptiScaler, ou la DLL d'un jeu avec FSR 4.1.",
    "{}: в этой DLL нет FSR 4. Нужна amd_fidelityfx_upscaler_dx12.dll версии 4.1.x.": "{} : cette DLL ne contient pas FSR 4. amd_fidelityfx_upscaler_dx12.dll version 4.1.x est nécessaire.",
    "Это не загрузчик": "Ce n'est pas le loader",
    "{} — это DLL апскейлера. Загрузчик называется amd_fidelityfx_loader_dx12.dll (у OptiScaler — amd_fidelityfx_dx12.dll) и лежит в той же папке игры, что и DLL апскейлера.": "{} est la DLL de l'upscaler. Le loader s'appelle amd_fidelityfx_loader_dx12.dll (amd_fidelityfx_dx12.dll dans OptiScaler) et se trouve dans le même dossier de jeu que la DLL de l'upscaler.",
    "{}: версия {}. Нужен загрузчик FidelityFX 2.x — из той же игры, что и DLL апскейлера.": "{} : version {}. Un loader FidelityFX 2.x est nécessaire, provenant du même jeu que la DLL de l'upscaler.",
    "Рядом с DLL нет загрузчика: выберите amd_fidelityfx_loader_dx12.dll из папки игры": "Pas de loader à côté de la DLL : choisissez amd_fidelityfx_loader_dx12.dll dans le dossier du jeu",
    "Собрать FSR 4.1.1 из amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: папка FSR4_LATEST, или из игры с FSR 4.1). Нужен GE-Proton 10+, Proton Experimental или Proton-CachyOS; 2–5 минут (RDNA4: вдвое дольше, ещё и вариант FP8)": "Générez FSR 4.1.1 à partir de amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler : le dossier FSR4_LATEST, ou celle d'un jeu avec FSR 4.1). Nécessite GE-Proton 10+, Proton Experimental ou Proton-CachyOS ; 2 à 5 minutes (RDNA4 : deux fois plus long, avec la variante FP8)",
    "Сборка не удалась (код {}): подробности в журнале": "La génération a échoué (code {}) : détails dans le journal",
    "Сглаживание в разрешении вывода без модели FSR": "Anticrénelage à la résolution de sortie, sans modèle FSR",
    "Нет или повреждён файл {}": "Fichier {} manquant ou endommagé",
    "Пропуск заставок при запуске": "Passer les vidéos d'introduction",
    "Частота кадров": "Fréquence d'images",
    "Режим": "Mode",
    "Какой патч частоты кадров применить к игре": "Quel correctif de fréquence d'images appliquer au jeu",
    "Без ограничения (патч)": "Illimitée (correctif)",
    "60 (как на PS4)": "60 (comme sur PS4)",
    "Ограничение FPS": "Limite de FPS",
    "0 — без ограничения; укажите число, чтобы ограничить FPS": "0 : aucune limite ; indiquez un nombre pour plafonner la fréquence d'images",
    "Производительность": "Performances",
    "Двухстадийный конвейер GPU": "Pipeline GPU à deux étapes",
    "Быстрее на 20–30%; при нестабильности выключите": "20 à 30 % plus rapide ; désactivez en cas d'instabilité",
    "Авто": "Auto",
    "Включён при 8 и более потоках процессора": "Activé avec 8 threads CPU ou plus",
    "Включён": "Activé",
    "Стабильнее, но медленнее": "Plus stable, mais plus lent",
    "Чтение данных GPU процессором": "Relecture des données GPU par le CPU",
    "По умолчанию": "Par défaut",
    "Фоновая загрузка в видеопамять": "Préchargement en arrière-plan dans la VRAM",
    "Меньше рывков при подгрузке зон": "Moins de saccades lors du chargement des zones",
    "Обычная": "Normal",
    "Без лишней видеопамяти": "Pas de VRAM supplémentaire",
    "Полная": "Complet",
    "Около 3 ГБ видеопамяти сверху": "Environ 3 Go de VRAM en plus",
    "Режим работы": "Mode",
    "Синхронизация как в 0.3": "Synchronisation comme dans la 0.3",
    "Для поиска регрессий: старая модель памяти и ожидания копий как в релизе 0.3": "Pour trouver des régressions : l'ancien modèle de mémoire et les attentes de copie tels que publiés dans la 0.3",
    "Выключена": "Désactivé",
    "Выключены": "Désactivé",
    "Для разработчика": "Développeur",
    "Статистика кадров в журнале": "Statistiques d'images dans le journal",
    "Сохранять журнал и статистику в файл": "Enregistrer le journal et les statistiques dans un fichier",
    "Диагностика вылетов": "Diagnostic des plantages",
    "Проверяет кучу игры и записывает записи в её память; немного медленнее": "Vérifie le tas du jeu et journalise les écritures dans sa mémoire ; un peu plus lent",
    "В папку logs в каталоге данных: для разбора рывков и вылетов": "Dans le dossier logs du répertoire de données : pour analyser les saccades et les plantages",
    "Профиль GPU в журнале": "Profil GPU dans le journal",
    "Слои валидации Vulkan": "Couches de validation Vulkan",
    "Сильно замедляет": "Beaucoup plus lent",
    "Доп. переменные (ИМЯ=значение через пробел)": "Variables supplémentaires (NOM=valeur, séparées par des espaces)",
    # Add to Steam
    "Добавить в Steam": "Ajouter à Steam",
    "Игра в библиотеке Steam запускается сразу, с настройками этого лаунчера": "Depuis la bibliothèque Steam, le jeu démarre directement avec les réglages de ce launcher",
    "Добавить": "Ajouter",
    "Steam не найден (или в него ещё никто не входил)": "Steam est introuvable (ou personne ne s'y est encore connecté)",
    "Закройте Steam и нажмите «Добавить» ещё раз": "Fermez Steam et cliquez à nouveau sur Ajouter",
    "Пока игра добавляется, Steam нужно закрыть; потом он запустится снова. Закрыть Steam?": "Steam doit être fermé pendant l'ajout du jeu ; il redémarre ensuite. Fermer Steam ?",
    "Отмена": "Annuler",
    "Закрыть Steam": "Fermer Steam",
    "Steam не закрылся. Закройте его сами и попробуйте ещё раз": "Steam ne s'est pas fermé. Fermez-le vous-même et réessayez",
    "Не удалось добавить игру в Steam: {}": "Impossible d'ajouter le jeu à Steam : {}",
    # Online page
    "Онлайн": "En ligne",
    "Играть онлайн": "Jouer en ligne",
    "Выключено: игра остаётся офлайн, как раньше": "Désactivé : le jeu reste hors ligne, comme avant",
    "Учётная запись": "Compte",
    "Пароль": "Mot de passe",
    "Соединение": "Connexion",
    "Проверить соединение": "Tester la connexion",
    "Проверить": "Tester",
    "Сервер shadNet": "Serveur shadNet",
    "Проверка…": "Vérification…",
    "доступен": "accessible",
    "недоступен": "inaccessible",
    # Button prompts
    "Применяется при запуске игры": "S'applique au lancement du jeu",
    "Поменять местами A и B": "Inverser A et B",
    "Для контроллеров в стиле Nintendo: подтверждение на A, отмена на B. Применяется при запуске игры": "Pour les manettes de type Nintendo : valider avec A, retour avec B. Appliqué au lancement du jeu",
    "Поменять стики местами": "Inverser les sticks",
    "Инвертировать камеру геймпада по горизонтали": "Inverser la caméra de la manette horizontalement",
    "Инвертировать камеру геймпада по вертикали": "Inverser la caméra de la manette verticalement",
    "Импортировать сохранения…": "Importer des sauvegardes…",
    "Импорт сохранений": "Importer des sauvegardes",
    "Это копия с PS4 на флешке (sdimg_*): она зашифрована ключами консоли. Экспортируйте сохранение без шифрования на PS4 (Apollo Save Tool) или через Save Wizard": "C’est une copie PS4 pour clé USB (sdimg_*) : elle est chiffrée avec les clés de la console. Exportez la sauvegarde non chiffrée sur la PS4 (Apollo Save Tool) ou avec Save Wizard",
    "Импортировать сохранения?": "Importer les sauvegardes ?",
    "Из {} (изменены {}). Текущие сохранения сначала копируются в {}": "Depuis {} (modifiées le {}). Les sauvegardes actuelles sont d’abord copiées dans {}",
    "Импортировать": "Importer",
    "Не удалось импортировать сохранения": "Impossible d’importer les sauvegardes",
    "Сохранения импортированы": "Sauvegardes importées",
    # Add to Steam with Flathub's Steam
    'Steam из Flatpak запускает игры в своей песочнице, где нет ни папки игры, ни драйверов: ярлык должен запускать игру вне её (flatpak-spawn --host). Для этого Steam нужно право org.freedesktop.Flatpak, с которым он может запускать программы в вашей системе. Выдать его?':
        "Steam en Flatpak lance les jeux dans son bac à sable, qui n'a ni le dossier du jeu ni les pilotes : le raccourci doit lancer le jeu en dehors (flatpak-spawn --host). Pour cela, Steam a besoin de l'autorisation org.freedesktop.Flatpak, qui lui permet de lancer des programmes sur votre système. L'accorder ?",
    'Выдать право':
        "Accorder l'autorisation",
    'Не удалось выдать право Steam: {}':
        "Impossible d'accorder l'autorisation à Steam : {}",
    "Копировать":
        "Copier",
    "Экспорт журнала…":
        "Exporter le journal…",
    "Экспорт журнала":
        "Exporter le journal",
    "Журнал скопирован":
        "Journal copié",
    "Журнал сохранён: {}":
        "Journal enregistré : {}",
    "Не удалось сохранить журнал: {}":
        "Impossible d'enregistrer le journal : {}",
    "Монитор":
        "Écran",
    "Основной":
        "Principal",
    ", основной":
        ", principal",
    "Новая: видеокарта работает с памятью игры напрямую, как в игре для ПК, а команды графики переводятся, а не эмулируются. Старая — модель памяти 0.3 со всеми исправлениями. Если драйвер не проходит проверку при запуске — старая":
        "Le nouveau : la carte graphique travaille directement avec la mémoire du jeu, comme dans un jeu PC, et les commandes graphiques sont traduites au lieu d'être émulées. L'ancien : le modèle mémoire de la 0.3 avec toutes les corrections. Si le pilote échoue à la vérification au démarrage, l'ancien",
    "Модель памяти и трансляции":
        "Modèle de mémoire et de traduction",
    "Авто: новая на AMD, старая на других":
        "Auto : nouveau sur AMD, ancien sur les autres",
    "Новая":
        "Nouveau",
    "Старая (как в 0.3)":
        "Ancien (comme dans la 0.3)",
    "О программе":
        "À propos",
    "Сначала закройте игру":
        "Fermez d'abord le jeu",
    "Основано на bbport от deadinside28":
        "Basé sur bbport de deadinside28",
    "Лицензия":
        "Licence",
    'GNU GPL v2 или новее · Файлы игры не входят.': 'GNU GPL v2 ou ultérieure · Aucun fichier du jeu inclus.',
    # 0.51: mouse look, choosing NVIDIA's DLSS library, the online module
    'DLSS {}: готово':
        'DLSS {} : prêt',
    'DLSS найден (нужна видеокарта NVIDIA RTX)':
        'DLSS trouvé (nécessite un GPU NVIDIA RTX)',
    'DLSS не найден: выберите библиотеку NVIDIA ниже (и нужна сборка с мостом DLSS). Игра включит FSR 3.1':
        'DLSS introuvable : choisissez la bibliothèque NVIDIA ci-dessous (une version avec le pont DLSS est aussi nécessaire). Le jeu utilisera FSR 3.1',
    'DLSS: библиотека NVIDIA':
        'DLSS : bibliothèque NVIDIA',
    '{} — библиотека DLSS для Windows; на Linux NVIDIA её не загружает. Нужна libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        '{} est la bibliothèque DLSS pour Windows ; le pilote NVIDIA pour Linux ne la charge pas. Il faut libnvidia-ngx-dlss.so.<version> du DLSS SDK de NVIDIA : {}',
    'Библиотека DLSS NVIDIA (libnvidia-ngx-dlss.so.*)':
        'Bibliothèque DLSS de NVIDIA (libnvidia-ngx-dlss.so.*)',
    'Выбрать файл…':
        'Choisir un fichier…',
    'Из сборки: {}':
        'De cette version : {}',
    'Инвертировать мышь по вертикали':
        "Inverser l'axe Y de la souris",
    'Камера мышью':
        'Caméra à la souris',
    'Клавиатура и мышь':
        'Clavier et souris',
    'Не удалось прочитать файл':
        'Impossible de lire le fichier',
    'Не удалось скопировать библиотеку':
        'Impossible de copier la bibliothèque',
    'Нет: выберите libnvidia-ngx-dlss.so.* из DLSS SDK NVIDIA ({})':
        'Aucune : choisissez libnvidia-ngx-dlss.so.* du DLSS SDK de NVIDIA ({})',
    'Нужен файл libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        'Il faut libnvidia-ngx-dlss.so.<version> du DLSS SDK de NVIDIA : {}',
    'Нужна библиотека для Linux':
        'Une bibliothèque pour Linux est nécessaire',
    'Своя: {}':
        'La vôtre : {}',
    'Убрать выбранную':
        'Retirer celle choisie',
    'Чувствительность мыши':
        'Sensibilité de la souris',
    'Щелчок в окне игры захватывает мышь, F1 — отпускает':
        'Un clic dans la fenêtre du jeu capture la souris, F1 la libère',
    'Эта сборка без модуля онлайна (libbbnet.so): игра только офлайн':
        "Cette version n'a pas le module en ligne (libbbnet.so) : jeu hors ligne uniquement",
    'Эта сборка без моста DLSS (libbbport_dlss.so): DLSS работать не будет':
        "Cette version n'a pas le pont DLSS (libbbport_dlss.so) : DLSS ne fonctionnera pas",
    'Это не библиотека DLSS':
        "Ce n'est pas la bibliothèque DLSS",
    # Online page: the server
    'Адрес сервера (host:port)':
        'Adresse du serveur (hôte:port)',
    'Сервер shadNet':
        'Serveur shadNet',
    # Trophies page
    'В дампе игры нет трофеев (sce_sys/trophy)':
        'Le dump du jeu n’a pas de trophées (sce_sys/trophy)',
    'Записываются, когда игра их открывает, и показываются в игре':
        'Enregistrés quand le jeu les débloque, et affichés dans le jeu',
    'Ключ трофеев':
        'Clé des trophées',
    'Неверный ключ трофеев: названия недоступны':
        'Clé des trophées incorrecte : les noms ne sont pas disponibles',
    'Получен {}':
        'Obtenu le {}',
    'Получено {} из {}':
        '{} sur {} obtenus',
    'Скрытый трофей':
        'Trophée caché',
    'Трофеи':
        'Trophées',
    'Платиновый':
        'Platine',
    'Золотой':
        'Or',
    'Серебряный':
        'Argent',
    'Бронзовый':
        'Bronze',
    "Вход в shadNet": "Connexion à shadNet",
    "неверное имя или пароль": "nom ou mot de passe incorrect",
    "такой учётной записи нет на этом сервере": "ce compte n'existe pas sur ce serveur",
    "эта учётная запись уже в сети (игра запущена?)": "ce compte est déjà connecté (le jeu est-il lancé ?)",
    "вход выполнен": "connecté",
    "вход не удался ({})": "échec de la connexion ({})",
    # About: Thanks
    'Благодарности': 'Remerciements',
    'Без них ничего этого не было бы': 'Sans eux, rien de tout cela ne serait possible',
    'Порт и его код': 'Le port et son code',
    'Помощь и тесты': 'Aide et tests',
    'Другие благодарности': 'Merci aussi à',
    'bbport — порт, на котором построен весь этот проект': 'bbport, le port sur lequel repose tout ce projet',
    'Игра по сети, DLSS, страница читов, добавление в Steam, значок, пропуск конвейеров, которые драйвер не может создать, и игра без вылета при нехватке видеопамяти': 'Jeu en ligne, DLSS, la page des triches, Ajouter à Steam, l’icône, ignorer les pipelines que le pilote ne peut pas créer et plus de plantage quand la mémoire vidéo manque',
    'Собрал и адаптировал десятки исправлений: вылеты при загрузке, чёрные изображения, апскейлер, строка производительности в журнале': 'A rassemblé et adapté des dizaines de correctifs : plantages au chargement, images noires, l’upscaler, la ligne de performances du journal',
    'Чёрный предпросмотр персонажа, картинка экрана загрузки и память кэша текстур': 'L’aperçu noir du personnage, l’image de l’écran de chargement et la mémoire du cache de textures',
    'Кэш текстур вовремя освобождает видеопамять': 'Le cache de textures libère la mémoire vidéo à temps',
    'Вылеты при загрузке областей': 'Plantages au chargement des zones',
    'Интерфейс, пропадавший не в 1080p, векторы движения больших чудовищ и ошибка памяти': 'L’interface qui disparaissait hors 1080p, les vecteurs de mouvement des grandes bêtes et une erreur mémoire',
    'Вылеты при загрузке некоторых карт и меню жестов с клавиатуры': 'Plantages au chargement de certaines cartes et le menu des gestes au clavier',
    'Экранная клавиатура для имени персонажа и уведомление о компиляции шейдеров': 'Le clavier à l’écran pour le nom du personnage et l’avis de compilation des shaders',
    'Сетевые библиотеки игры по сети и сервер для своего кооператива': 'Les bibliothèques du jeu en ligne et le serveur pour votre propre coopération',
    'Основа поддержки DLSS и модель FSR 4 без шлейфов за персонажами': 'La base de la prise en charge de DLSS et le modèle FSR 4 sans traînées derrière les personnages',
    'Апскейлер FSR 3.1': 'L’upscaler FSR 3.1',
    'Игра запускается, когда DLSS нельзя использовать': 'Le jeu démarre quand DLSS ne peut pas être utilisé',
    'Перевод на упрощённый китайский': 'La traduction en chinois simplifié',
    'Звук игры на полной громкости': 'Le son du jeu à plein volume',
    'Флажки и ползунки внутриигрового меню': 'Les cases et les curseurs du menu en jeu',
    'Подробные отчёты с журналами и проверка исправлений': 'Rapports détaillés avec journaux et tests des correctifs',
    'Идея поменять местами A и B на контроллерах в стиле Nintendo': 'L’idée d’inverser A et B sur les manettes de style Nintendo',
    'Проверка исправления видеопамяти': 'Test du correctif de la mémoire vidéo',
    'Рендерер и компилятор шейдеров': 'Le moteur de rendu et le recompilateur de shaders',
    'Инструмент для сборки AppImage': 'L’outil qui crée l’AppImage',
    'Нашёл ошибку, из-за которой игра не запускалась на некоторых видеокартах, и ускорение камеры на DualShock 4': 'A trouvé le bug qui empêchait le jeu de démarrer sur certaines cartes graphiques, et l’accélération de la caméra sur DualShock 4',
    'Нашёл, почему игра не запускалась в игровом режиме Steam Deck': 'A trouvé pourquoi le jeu ne démarrait pas en mode Jeu sur le Steam Deck',
    'Нашёл, при каких эффектах зависают загрузки на NVIDIA': 'A trouvé quels effets figent les écrans de chargement sur NVIDIA',
    'ps4-pkg-extractor: установка игры из файлов .pkg': 'ps4-pkg-extractor : installer le jeu depuis des fichiers .pkg',
    # Shader cache
    'Кэш шейдеров': 'Cache des shaders',
    'Очистить': 'Vider',
    '{}. Если после обновления картинка выглядит странно, очистите его: шейдеры соберутся заново (первые минуты в каждой зоне возможны рывки)': '{}. Si l’image semble étrange après une mise à jour, videz-le : les shaders sont reconstruits (quelques saccades les premières minutes dans chaque zone)',
    'Пусто: шейдеры соберутся при игре': 'Vide : les shaders sont construits pendant que vous jouez',
    'Очистить кэш шейдеров?': 'Vider le cache des shaders ?',
    'Игра соберёт шейдеры заново: первые минуты в каждой зоне возможны рывки. Сохранения и настройки не затрагиваются.': 'Le jeu reconstruit les shaders : quelques saccades les premières minutes dans chaque zone. Les sauvegardes et les réglages ne sont pas touchés.',
    'Названия трофеев на английском без ключа и звук при получении трофея': 'Les noms des trophées en anglais sans la clé et le son à l’obtention d’un trophée',
    'Буфер трафарета, в который писали цветные изображения': 'Le tampon de stencil dans lequel écrivaient des images couleur',
    'Вход на публичный сервер shadNet без отключения': 'Rester connecté au serveur public shadNet',
    'Установить из PKG': 'Installer depuis des PKG',
    'Выбрать .pkg…': 'Choisir des .pkg…',
    'Файлы .pkg: игра, обновление, DLC': 'Fichiers .pkg : jeu, mise à jour, DLC',
    'Куда установить игру': 'Où installer le jeu',
    'Установка…': 'Installation…',
    'Игра установлена: {}': 'Jeu installé : {}',
    'Не удалось установить: подробности в журнале': 'Échec de l’installation : détails dans le journal',
    'Выход из игры из меню с контроллера, меню в пределах экрана и половины тачпада на Xbox': 'Quitter le jeu depuis le menu à la manette, le menu qui tient dans l’écran et les moitiés du pavé tactile sur les manettes Xbox',
    'Вылет видеоплеера при его остановке': 'Un plantage du lecteur vidéo à son arrêt',
    'Язык внутриигрового меню при запуске без окна лаунчера': 'La langue du menu en jeu au lancement sans la fenêtre du launcher',
    'DLSS в AppImage на NVIDIA': 'DLSS dans l’AppImage sur NVIDIA',
    'Сверхширокие мониторы без растянутой картинки': 'Les écrans ultra-larges sans image étirée',
    'Движение с клавиатуры: круглая диагональ и последняя нажатая клавиша': 'Déplacement au clavier : diagonale ronde et dernière touche pressée',
    'Отладка вылетов: процесс ждёт отладчик (BB_FAULT_WAIT)': 'Débogage des plantages : le processus attend un débogueur (BB_FAULT_WAIT)',
    'Видеопамять на картах с 4 ГБ и вылеты: флипы, swapchain, дескрипторы и ошибки страниц; смена стиков и инверсия камеры, импорт сохранений, выбор версии': 'Mémoire vidéo sur les cartes de 4 Go et plantages : flips, swapchain, descripteurs et défauts de page ; sticks inversés et caméra inversée, import des sauvegardes, choix de version',
    'Большие группы команд записи и swapchain после изменений экрана': 'Grands groupes de commandes enregistrées et la swapchain après un changement d’affichage',
    # GODZILLA (gzport)
    'GODZILLA {}, версия 1.01':
        'GODZILLA {}, version 1.01',
    'GODZILLA добавлена в библиотеку Steam':
        'GODZILLA ajouté à la bibliothèque Steam',
    'GODZILLA — товарный знак Toho Co., Ltd.; игра для PS4 издана Bandai Namco Entertainment. Этот проект с ними не связан.':
        "GODZILLA est une marque de Toho Co., Ltd. ; le jeu PS4 a été édité par Bandai Namco Entertainment. Ce projet n'a aucun lien avec elles.",
    'XML-патчи в формате shadPS4 для версии 01.01 из папки патчей. Применяются при запуске.':
        'Correctifs XML au format shadPS4 pour la version 01.01, depuis le dossier des correctifs. Appliqués au démarrage.',
    'eboot.bin не от версии 1.01: скопируйте eboot.bin из дампа обновления 1.01 в папку игры с заменой':
        "eboot.bin n'est pas celui de la 1.01 : copiez eboot.bin de la mise à jour 1.01 extraite dans le dossier du jeu, en le remplaçant",
    'gzport — нативный порт для Linux':
        'gzport — portage natif pour Linux',
    'Авторы bbport и bloodborne_linux, на которых построен gzport, и все, кто им помогал':
        'Les auteurs de bbport et de bloodborne_linux, sur lesquels gzport est construit, et tous ceux qui les ont aidés',
    'В папке игры нет: {}. Распакуйте игру и обновление 1.01 заново':
        'Absent du dossier du jeu : {}. Extrayez de nouveau le jeu et la mise à jour 1.01',
    'В этой папке нет сохранений GODZILLA (SAVEDATA00 с DATA.BIN)':
        'Aucune sauvegarde de GODZILLA dans ce dossier (SAVEDATA00 avec DATA.BIN)',
    'Игра идёт с 60 FPS, как на PS4. Выше 60 FPS: нужен патч частоты кадров, его пока нет':
        "Le jeu tourne à 60 FPS, comme sur PS4. Au-delà de 60 FPS, il faut un correctif de fréquence d'images, pas encore disponible",
    'Для GODZILLA пока недоступен: игра рисует кадр прямо в разрешении вывода':
        'Pas encore disponible pour GODZILLA : le jeu dessine l\'image directement à la résolution de sortie',
    'Игра, обновление 1.01 и DLC из ваших файлов .pkg':
        'Le jeu, la mise à jour 1.01 et les DLC depuis vos fichiers .pkg',
    'Ключ трофеев PS4 (TrophyKey в shadPS4), 32 шестнадцатеричных символа: с ним названия и описания на языке игры. Хранится на этом компьютере. Без него видны только значки':
        'La clé des trophées PS4 (TrophyKey dans shadPS4), 32 chiffres hexadécimaux : avec elle, les noms et descriptions sont dans la langue du jeu. Conservée sur cet ordinateur. Sans elle, seules les icônes sont visibles',
    'Нативный порт для Linux, версия {}':
        'Portage natif pour Linux, version {}',
    'Нужен патч для версии 1.01, его пока нет':
        'Nécessite un correctif pour la version 1.01, pas encore disponible',
    'Нужно обновление 1.01: скопируйте файлы дампа обновления 1.01 в папку игры с заменой (найдена версия {})':
        'La mise à jour 1.01 est nécessaire : copiez la mise à jour 1.01 extraite dans le dossier du jeu, en remplaçant les fichiers (version trouvée : {})',
    'Основано на bloodborne_linux от ayozetr':
        'Basé sur bloodborne_linux par ayozetr',
    'bloodborne_linux: порт для Linux, на котором построен gzport':
        'bloodborne_linux : le portage Linux sur lequel gzport est construit',
    'Папка с сохранениями GODZILLA':
        'Dossier des sauvegardes de GODZILLA',
    'Патчи игры':
        'Correctifs du jeu',
    'Португальский (Бразилия)':
        'Portugais (Brésil)',
    'Это не GODZILLA (найдено {}): нужна GODZILLA (CUSA02046) с обновлением 1.01':
        "Ce n'est pas GODZILLA (trouvé : {}) : il faut GODZILLA (CUSA02046) avec la mise à jour 1.01",
    'Тачпад, левая половина':
        'Pavé tactile, moitié gauche',
    'Тачпад, правая половина':
        'Pavé tactile, moitié droite',
    'Настройки по умолчанию':
        'Valeurs par défaut',
    'Восстановить мои настройки по умолчанию':
        'Restaurer mes valeurs par défaut',
    'Вернуть':
        'Restaurer',
    'Сохранить текущие как мои настройки по умолчанию':
        'Enregistrer les réglages actuels comme mes valeurs par défaut',
    'Настройки лаунчера и bbport.ini, без назначений кнопок':
        'Réglages du lanceur et de bbport.ini, sans les affectations des boutons',
    'Сохранить':
        'Enregistrer',
    'Из {}':
        'Depuis {}',
    'Своих настроек по умолчанию пока нет: восстанавливаются встроенные (папки и ключ трофеев не меняются)':
        'Pas encore de valeurs par défaut personnelles : les valeurs intégrées sont restaurées (les dossiers et la clé des trophées restent)',
    'Не удалось прочитать {}':
        'Impossible de lire {}',
    'Восстановить настройки по умолчанию?':
        'Restaurer les valeurs par défaut ?',
    'Настройки лаунчера и bbport.ini станут такими, как в {}. Остальные строки bbport.ini, в том числе назначения кнопок, не меняются':
        'Les réglages du lanceur et de bbport.ini deviennent ceux de {}. Les autres lignes de bbport.ini, affectations des boutons comprises, ne changent pas',
    'Своих настроек по умолчанию нет: настройки лаунчера и bbport.ini станут встроенными. Папки, ключ трофеев и назначения кнопок не меняются':
        'Pas de valeurs par défaut personnelles : les réglages du lanceur et de bbport.ini reviennent aux valeurs intégrées. Les dossiers, la clé des trophées et les affectations des boutons ne changent pas',
    'Настройки по умолчанию восстановлены':
        'Valeurs par défaut restaurées',
    'Сохранить текущие настройки как свои по умолчанию?':
        'Enregistrer les réglages actuels comme vos valeurs par défaut ?',
    'Они запишутся в {} вместо прежних, и «Вернуть» будет восстанавливать их':
        'Ils sont écrits dans {} à la place des précédents, et « Restaurer » y revient',
    'Не удалось сохранить {}':
        "Impossible d'enregistrer {}",
    'Текущие настройки сохранены как ваши по умолчанию':
        'Réglages actuels enregistrés comme vos valeurs par défaut',
    # Online page (LAN versus)
    "Версус по локальной сети: VS MODE в меню «Онлайн» игры, через ваш сервер shadNet (shadnet-p2p с патчем gzport). У каждого игрока своя учётная запись на этом сервере": "Versus en réseau local : VS MODE dans le menu « Online » du jeu, via votre propre serveur shadNet (shadnet-p2p avec le correctif gzport). Chaque joueur a son propre compte sur ce serveur",
    "Как настроить версус по сети": "Configurer le versus en réseau",
    "Имя учётной записи на сервере shadNet (оно же ваше имя в игре) и её пароль. Пароль хранится на этом компьютере вместе с настройками лаунчера": "Le nom de votre compte sur le serveur shadNet (c'est aussi votre nom dans le jeu) et son mot de passe. Le mot de passe est enregistré sur cet ordinateur avec les réglages du lanceur",
    "Порт P2P (UDP)": "Port P2P (UDP)",
    "Через него игроки соединяются напрямую; он должен быть открыт между компьютерами": "Les joueurs se connectent directement par ce port ; il doit être ouvert entre les ordinateurs",
    "Укажите адрес сервера": "Indiquez l'adresse du serveur",
    "UDP сервера shadNet": "UDP du serveur shadNet",
    "отвечает; сервер видит этот компьютер как {}": "répond ; le serveur voit cet ordinateur comme {}",
    "не отвечает: матч не соединится": "pas de réponse : la partie ne se connectera pas",
}


# German.
DE = {
    "Папка DLC": "DLC-Ordner",
    "Выбрать папку DLC": "DLC-Ordner wählen",
    "Не использовать DLC": "Keine DLC verwenden",
    "Найдено DLC: {}": "Gefundene DLC: {}",
    "Не используется": "Nicht verwendet",
    "Нет DLC этой игры в папке": "Keine DLC dieses Spiels im Ordner",
    "Запустить": "Spielen",
    "Остановить": "Stoppen",
    "Настройки": "Einstellungen",
    "Журнал": "Protokoll",
    "Не удалось запустить: {}": "Start fehlgeschlagen: {}",
    "\n— игра завершилась (код {}) —\n": "\n— das Spiel wurde beendet (Code {}) —\n",
    "Язык лаунчера": "Sprache des Launchers",
    "Как в системе": "System",
    "Применится после перезапуска лаунчера, пока игра запущена": "Wird nach einem Neustart des Launchers übernommen, sobald das Spiel läuft",
    "Игра": "Spiel",
    "Папка игры ({})": "Spielordner ({})",
    "Папка игры": "Spielordner",
    "Выбрать папку с eboot.bin": "Ordner mit eboot.bin auswählen",
    "Открыть в файловом менеджере": "Im Dateimanager öffnen",
    "Папка сохранений": "Ordner für Spielstände",
    "Выбрать папку сохранений": "Ordner für Spielstände auswählen",
    "Вернуть папку по умолчанию": "Zurück zum Standardordner",
    "Язык системы": "Systemsprache",
    "По умолчанию: {}": "Standard: {}",
    "Найдены сохранения": "Spielstände gefunden",
    "Сохранений пока нет: игра создаст их здесь": "Noch keine Spielstände: Das Spiel legt sie hier an",
    "не выбрана": "nicht ausgewählt",
    "Нет eboot.bin в папке": "Keine eboot.bin im Ordner",
    "Управление": "Steuerung",
    "Геймпад": "Gamepad",
    "Назначение кнопок; применяется при запуске игры": "Tastenbelegung; wird beim Spielstart übernommen",
    "Назначить": "Zuweisen",
    "Сбросить": "Zurücksetzen",
    "{} (по умолчанию)": "{} (Standard)",
    "не назначено": "nicht zugewiesen",
    "Нажмите клавишу или кнопку… (Esc — отмена)": "Drücke eine Taste oder einen Knopf … (Esc bricht ab)",
    "Крест": "Kreuz",
    "Круг": "Kreis",
    "Квадрат": "Quadrat",
    "Треугольник": "Dreieck",
    "Крестовина вверх": "Steuerkreuz oben",
    "Крестовина вниз": "Steuerkreuz unten",
    "Крестовина влево": "Steuerkreuz links",
    "Крестовина вправо": "Steuerkreuz rechts",
    "Движение вперёд": "Vorwärts bewegen",
    "Движение назад": "Rückwärts bewegen",
    "Движение влево": "Nach links bewegen",
    "Движение вправо": "Nach rechts bewegen",
    "Камера вверх": "Kamera nach oben",
    "Камера вниз": "Kamera nach unten",
    "Камера влево": "Kamera nach links",
    "Камера вправо": "Kamera nach rechts",
    "Контроллер": "Controller",
    "Выбранный берётся, как только подключится": "Der ausgewählte Controller wird verwendet, sobald er verbunden ist",
    "Первый подключённый": "Zuerst verbundener",
    "{} (не подключён)": "{} (nicht verbunden)",
    "eboot.bin не читается как расшифрованный исполняемый файл PS4: сделайте дамп заново": "Die eboot.bin lässt sich nicht als entschlüsselte PS4-Programmdatei lesen: Erstelle den Dump des Spiels erneut",
    "Папка игры (с eboot.bin)": "Spielordner (mit eboot.bin)",
    "Английский": "Englisch",
    "Русский": "Russisch",
    "Французский": "Französisch",
    "Испанский": "Spanisch",
    "Обновить список": "Liste aktualisieren",
    "Сторонние патчи": "Patches von Drittanbietern",
    "Папка патчей": "Patches-Ordner",
    "Выбрать папку патчей": "Patches-Ordner auswählen",
    "Открыть папку патчей": "Patches-Ordner öffnen",
    "Патчей нет": "Keine Patches",
    "Автор: {}": "Autor: {}",
    "Экран": "Anzeige",
    "Разрешение вывода": "Ausgabeauflösung",
    "Апскейлер дорисовывает кадр; Steam Deck — 720p": "Der Upscaler füllt das Bild aus; Steam Deck: 720p",
    "Полноэкранный режим": "Vollbild",
    "Смена разрешения на лету": "Auflösungswechsel im laufenden Betrieb",
    "Без перезапуска, но медленнее на Steam Deck и старых GPU": "Kein Neustart nötig, aber langsamer auf dem Steam Deck und älteren GPUs",
    "Авто (по видеокарте)": "Auto (je nach GPU)",
    "Выключена (быстрее)": "Aus (schneller)",
    "Включена": "An",
    "Режим показа кадров": "Präsentationsmodus",
    "Разрешить HDR": "HDR zulassen",
    "Апскейлер": "Upscaler",
    "Хранится в bbport.ini; в игре меняется через меню (Insert или L3+R3)": "Wird in bbport.ini gespeichert; im Spiel änderst du es im Menü (Insert oder L3+R3)",
    "TAA (нативное сглаживание)": "TAA (native Kantenglättung)",
    "Выключен": "Aus",
    "Пресет": "Voreinstellung",
    "Резкость (RCAS)": "Schärfen (RCAS)",
    "Сила резкости": "Schärfe",
    "Векторы движения объектов": "Bewegungsvektoren von Objekten",
    "Меньше гостинга на персонажах; стоит около 10% FPS": "Weniger Geisterbilder bei Figuren; kostet etwa 10 % FPS",
    "Показывать FPS": "FPS anzeigen",
    "Ассеты найдены": "Assets gefunden",
    "Нет ассетов: tools/fetch_fsr4_assets.sh": "Keine Assets: tools/fetch_fsr4_assets.sh",
    "Ассеты для выбранного режима найдены": "Assets für den gewählten Modus gefunden",
    "{}. Соберите FSR 4.1.1 из своей DLL кнопкой «Выбрать DLL…» ниже": "{}. Erstelle FSR 4.1.1 aus deiner eigenen DLL über die Schaltfläche „DLL auswählen …“ unten",
    "FSR 4.1.1 из своей DLL AMD": "FSR 4.1.1 aus deiner eigenen AMD-DLL",
    "Отменить": "Abbrechen",
    "Выбрать DLL…": "DLL auswählen …",
    "DLL апскейлера AMD (amd_fidelityfx_upscaler_dx12.dll)": "AMD-Upscaler-DLL (amd_fidelityfx_upscaler_dx12.dll)",
    "нет": "keine",
    "Эта DLL не подходит": "Diese DLL passt nicht",
    "{}: версия {}, модели FSR 4: {}.\n\nbbport повторяет только официальную FSR 4.1.x от AMD (модель v07_fp8_no_scale): например, FSR4_LATEST из OptiScaler или amd_fidelityfx_upscaler_dx12.dll из игры с FSR 4.1. Сборки сообщества (4.0.2b и подобные) устроены иначе и пока не поддерживаются.": "{}: Version {}, FSR-4-Modelle: {}.\n\nbbport gibt nur das offizielle AMD FSR 4.1.x wieder (Modell v07_fp8_no_scale): zum Beispiel FSR4_LATEST von OptiScaler oder amd_fidelityfx_upscaler_dx12.dll aus einem Spiel mit FSR 4.1. Community-Builds (4.0.2b und ähnliche) sind anders aufgebaut und werden noch nicht unterstützt.",
    "Загрузчик не подходит": "Der Loader passt nicht",
    "Загрузчик FidelityFX (amd_fidelityfx_loader_dx12.dll или amd_fidelityfx_dx12.dll)": "FidelityFX-Loader (amd_fidelityfx_loader_dx12.dll oder amd_fidelityfx_dx12.dll)",
    "\n— сборка FSR 4.1.1 из {} —\n": "\n— FSR 4.1.1 wird aus {} erstellt —\n",
    "Подготовка…": "Wird vorbereitet …",
    "Запись проходов DLL под Proton: {} из {}": "Die Durchläufe der DLL werden unter Proton aufgezeichnet: {} von {}",
    "Перевод проходов в SPIR-V…": "Durchläufe werden in SPIR-V übersetzt …",
    "— сборка FSR 4.1.1 завершилась (код {}) —\n": "— Erstellung von FSR 4.1.1 beendet (Code {}) —\n",
    "FSR 4.1.1 собран и выбран": "FSR 4.1.1 erstellt und ausgewählt",
    "Сборка FSR 4.1.1 отменена": "Erstellung von FSR 4.1.1 abgebrochen",
    "FSR 4.1.1 не собран": "FSR 4.1.1 wurde nicht erstellt",
    "DLL не подходит: подробности в журнале": "Die DLL passt nicht: Details im Protokoll",
    "Не хватает программ для сборки: список в журнале": "Werkzeuge für die Erstellung fehlen: Die Liste steht im Protokoll",
    "Записанные проходы не совпали с тем, что повторяет bbport (другая версия DLL или новая видеокарта?): подробности в журнале": "Die aufgezeichneten Durchläufe passen nicht zu dem, was bbport wiedergibt (andere DLL-Version oder neue GPU?): Details im Protokoll",
    "Не найден загрузчик FidelityFX 2.x": "Kein FidelityFX-Loader 2.x gefunden",
    "Не найден подходящий Proton: установите GE-Proton 10 или новее (ProtonUp-Qt) или Proton Experimental / Proton-CachyOS в Steam. Если они есть — запустите в Steam любую игру с этим Proton, чтобы Steam поставил его рантайм": "Kein passendes Proton gefunden: Installiere GE-Proton 10 oder neuer (ProtonUp-Qt) oder Proton Experimental / Proton-CachyOS in Steam. Wenn du sie hast, starte ein beliebiges Spiel mit diesem Proton in Steam, damit Steam dessen Runtime installiert",
    "Ни один Proton не запустил FSR 4.1 из этой DLL. Либо они слишком старые (подходят GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), либо DLL не включает FSR 4.1 на этой видеокарте (Steam Deck?): тогда соберите на ПК с Radeon RX 7000/9000 и скопируйте папку fsr4_411. Подробности в журнале": "Kein Proton hat FSR 4.1 dieser DLL gestartet. Entweder sind sie zu alt (GE-Proton 10+, Proton Experimental und Proton-CachyOS 11 funktionieren), oder die DLL aktiviert FSR 4.1 auf dieser GPU nicht (Steam Deck?): Erstelle es dann auf einem PC mit Radeon RX 7000/9000 und kopiere den Ordner fsr4_411. Details im Protokoll",
    "На NixOS запись идёт на самой системе (systemd --user) через umu-launcher из nix-shell, а здесь их не нашлось: установите umu-launcher или Nix. Подробности в журнале": "Unter NixOS läuft die Aufzeichnung direkt auf dem System (systemd --user) mit umu-launcher aus nix-shell, und keines von beiden wurde gefunden: Installiere umu-launcher oder Nix. Details im Protokoll",
    "{}: FSR {}. Это официальная FSR 4.0.x от AMD: она включается только на видеокартах RDNA4 (RX 9000), а под Proton на других видеокартах не запускается, поэтому записать её нельзя.\n\nНужна FSR 4.1.x: например, FSR4_LATEST из OptiScaler или DLL из игры с FSR 4.1.": "{}: FSR {}. Das ist das offizielle AMD FSR 4.0.x: Es ist nur auf RDNA4-GPUs (RX 9000) aktiviert und startet unter Proton auf anderen GPUs nicht, daher lässt es sich nicht aufzeichnen.\n\nBenötigt wird FSR 4.1.x: zum Beispiel FSR4_LATEST von OptiScaler oder die DLL eines Spiels mit FSR 4.1.",
    "{}: в этой DLL нет FSR 4. Нужна amd_fidelityfx_upscaler_dx12.dll версии 4.1.x.": "{}: Diese DLL enthält kein FSR 4. Benötigt wird amd_fidelityfx_upscaler_dx12.dll in Version 4.1.x.",
    "Это не загрузчик": "Das ist nicht der Loader",
    "{} — это DLL апскейлера. Загрузчик называется amd_fidelityfx_loader_dx12.dll (у OptiScaler — amd_fidelityfx_dx12.dll) и лежит в той же папке игры, что и DLL апскейлера.": "{} ist die Upscaler-DLL. Der Loader heißt amd_fidelityfx_loader_dx12.dll (bei OptiScaler amd_fidelityfx_dx12.dll) und liegt im selben Spielordner wie die Upscaler-DLL.",
    "{}: версия {}. Нужен загрузчик FidelityFX 2.x — из той же игры, что и DLL апскейлера.": "{}: Version {}. Benötigt wird ein FidelityFX-Loader 2.x aus demselben Spiel wie die Upscaler-DLL.",
    "Рядом с DLL нет загрузчика: выберите amd_fidelityfx_loader_dx12.dll из папки игры": "Kein Loader neben der DLL: Wähle amd_fidelityfx_loader_dx12.dll aus dem Ordner des Spiels",
    "Собрать FSR 4.1.1 из amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: папка FSR4_LATEST, или из игры с FSR 4.1). Нужен GE-Proton 10+, Proton Experimental или Proton-CachyOS; 2–5 минут (RDNA4: вдвое дольше, ещё и вариант FP8)": "Erstellt FSR 4.1.1 aus amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: der Ordner FSR4_LATEST, oder aus einem Spiel mit FSR 4.1). Benötigt GE-Proton 10+, Proton Experimental oder Proton-CachyOS; 2–5 Minuten (RDNA4: doppelt so lange, mit der FP8-Variante)",
    "Сборка не удалась (код {}): подробности в журнале": "Die Erstellung ist fehlgeschlagen (Code {}): Details im Protokoll",
    "Сглаживание в разрешении вывода без модели FSR": "Kantenglättung in Ausgabeauflösung, ohne FSR-Modell",
    "Нет или повреждён файл {}": "Datei {} fehlt oder ist beschädigt",
    "Пропуск заставок при запуске": "Intro-Videos überspringen",
    "Частота кадров": "Bildrate",
    "Режим": "Modus",
    "Какой патч частоты кадров применить к игре": "Welcher Bildraten-Patch auf das Spiel angewendet wird",
    "Без ограничения (патч)": "Unbegrenzt (Patch)",
    "60 (как на PS4)": "60 (wie auf der PS4)",
    "Ограничение FPS": "FPS-Limit",
    "0 — без ограничения; укажите число, чтобы ограничить FPS": "0: kein Limit; gib eine Zahl ein, um die Bildrate zu begrenzen",
    "Производительность": "Leistung",
    "Двухстадийный конвейер GPU": "Zweistufige GPU-Pipeline",
    "Быстрее на 20–30%; при нестабильности выключите": "20–30 % schneller; bei Instabilität ausschalten",
    "Авто": "Auto",
    "Включён при 8 и более потоках процессора": "An ab 8 CPU-Threads",
    "Включён": "An",
    "Стабильнее, но медленнее": "Stabiler, aber langsamer",
    "Чтение данных GPU процессором": "Auslesen von GPU-Daten durch die CPU",
    "По умолчанию": "Standard",
    "Фоновая загрузка в видеопамять": "Vorab-Upload in den VRAM im Hintergrund",
    "Меньше рывков при подгрузке зон": "Weniger Ruckler beim Nachladen von Bereichen",
    "Обычная": "Normal",
    "Без лишней видеопамяти": "Kein zusätzlicher VRAM",
    "Полная": "Voll",
    "Около 3 ГБ видеопамяти сверху": "Etwa 3 GB mehr VRAM",
    "Режим работы": "Modus",
    "Синхронизация как в 0.3": "Synchronisierung wie in 0.3",
    "Для поиска регрессий: старая модель памяти и ожидания копий как в релизе 0.3": "Zum Aufspüren von Regressionen: das alte Speichermodell und die Kopier-Wartezeiten wie in 0.3 veröffentlicht",
    "Выключена": "Aus",
    "Выключены": "Aus",
    "Для разработчика": "Entwickler",
    "Статистика кадров в журнале": "Bildstatistiken im Protokoll",
    "Сохранять журнал и статистику в файл": "Protokoll und Statistiken in einer Datei speichern",
    "Диагностика вылетов": "Absturzdiagnose",
    "Проверяет кучу игры и записывает записи в её память; немного медленнее": "Prüft den Heap des Spiels und protokolliert Schreibzugriffe in dessen Speicher; etwas langsamer",
    "В папку logs в каталоге данных: для разбора рывков и вылетов": "In den Ordner logs des Datenverzeichnisses: zur Analyse von Rucklern und Abstürzen",
    "Профиль GPU в журнале": "GPU-Profil im Protokoll",
    "Слои валидации Vulkan": "Vulkan-Validierungsebenen",
    "Сильно замедляет": "Deutlich langsamer",
    "Доп. переменные (ИМЯ=значение через пробел)": "Zusätzliche Variablen (NAME=Wert, durch Leerzeichen getrennt)",
    # Add to Steam
    "Добавить в Steam": "Zu Steam hinzufügen",
    "Игра в библиотеке Steam запускается сразу, с настройками этого лаунчера": "Aus der Steam-Bibliothek startet das Spiel direkt, mit den Einstellungen dieses Launchers",
    "Добавить": "Hinzufügen",
    "Steam не найден (или в него ещё никто не входил)": "Steam wurde nicht gefunden (oder es hat sich noch niemand angemeldet)",
    "Закройте Steam и нажмите «Добавить» ещё раз": "Schließe Steam und klicke erneut auf Hinzufügen",
    "Пока игра добавляется, Steam нужно закрыть; потом он запустится снова. Закрыть Steam?": "Steam muss geschlossen werden, während das Spiel hinzugefügt wird; danach startet es wieder. Steam schließen?",
    "Отмена": "Abbrechen",
    "Закрыть Steam": "Steam schließen",
    "Steam не закрылся. Закройте его сами и попробуйте ещё раз": "Steam wurde nicht geschlossen. Schließe es selbst und versuche es erneut",
    "Не удалось добавить игру в Steam: {}": "Spiel konnte nicht zu Steam hinzugefügt werden: {}",
    # Online page
    "Онлайн": "Online",
    "Играть онлайн": "Online spielen",
    "Выключено: игра остаётся офлайн, как раньше": "Aus: Das Spiel bleibt offline wie bisher",
    "Учётная запись": "Konto",
    "Пароль": "Passwort",
    "Соединение": "Verbindung",
    "Проверить соединение": "Verbindung testen",
    "Проверить": "Testen",
    "Сервер shadNet": "shadNet-Server",
    "Проверка…": "Prüfe…",
    "доступен": "erreichbar",
    "недоступен": "nicht erreichbar",
    # Button prompts
    "Применяется при запуске игры": "Wird beim Spielstart übernommen",
    "Поменять местами A и B": "A und B tauschen",
    "Для контроллеров в стиле Nintendo: подтверждение на A, отмена на B. Применяется при запуске игры": "Für Controller im Nintendo-Stil: Bestätigen mit A, Zurück mit B. Wird beim Spielstart übernommen",
    "Поменять стики местами": "Sticks tauschen",
    "Инвертировать камеру геймпада по горизонтали": "Controller-Kamera horizontal invertieren",
    "Инвертировать камеру геймпада по вертикали": "Controller-Kamera vertikal invertieren",
    "Импортировать сохранения…": "Spielstände importieren…",
    "Импорт сохранений": "Spielstände importieren",
    "Это копия с PS4 на флешке (sdimg_*): она зашифрована ключами консоли. Экспортируйте сохранение без шифрования на PS4 (Apollo Save Tool) или через Save Wizard": "Das ist eine PS4-Kopie für einen USB-Stick (sdimg_*): Sie ist mit den Schlüsseln der Konsole verschlüsselt. Exportiere den Spielstand unverschlüsselt auf der PS4 (Apollo Save Tool) oder mit Save Wizard",
    "Импортировать сохранения?": "Spielstände importieren?",
    "Из {} (изменены {}). Текущие сохранения сначала копируются в {}": "Aus {} (geändert {}). Die aktuellen Spielstände werden zuerst nach {} kopiert",
    "Импортировать": "Importieren",
    "Не удалось импортировать сохранения": "Die Spielstände konnten nicht importiert werden",
    "Сохранения импортированы": "Spielstände importiert",
    # Add to Steam with Flathub's Steam
    'Steam из Flatpak запускает игры в своей песочнице, где нет ни папки игры, ни драйверов: ярлык должен запускать игру вне её (flatpak-spawn --host). Для этого Steam нужно право org.freedesktop.Flatpak, с которым он может запускать программы в вашей системе. Выдать его?':
        'Steam aus Flatpak startet Spiele in seiner Sandbox, in der weder der Spielordner noch die Treiber sind: Die Verknüpfung muss das Spiel außerhalb davon starten (flatpak-spawn --host). Dafür braucht Steam die Berechtigung org.freedesktop.Flatpak, mit der es Programme auf deinem System starten kann. Erteilen?',
    'Выдать право':
        'Berechtigung erteilen',
    'Не удалось выдать право Steam: {}':
        'Steam konnte die Berechtigung nicht erteilt werden: {}',
    "Копировать":
        "Kopieren",
    "Экспорт журнала…":
        "Protokoll exportieren…",
    "Экспорт журнала":
        "Protokoll exportieren",
    "Журнал скопирован":
        "Protokoll kopiert",
    "Журнал сохранён: {}":
        "Protokoll gespeichert: {}",
    "Не удалось сохранить журнал: {}":
        "Protokoll konnte nicht gespeichert werden: {}",
    "Монитор":
        "Monitor",
    "Основной":
        "Hauptmonitor",
    ", основной":
        ", Hauptmonitor",
    "Новая: видеокарта работает с памятью игры напрямую, как в игре для ПК, а команды графики переводятся, а не эмулируются. Старая — модель памяти 0.3 со всеми исправлениями. Если драйвер не проходит проверку при запуске — старая":
        "Das neue: Die Grafikkarte arbeitet direkt mit dem Speicher des Spiels, wie bei einem PC-Spiel, und Grafikbefehle werden übersetzt statt emuliert. Das alte: das Speichermodell von 0.3 mit allen Korrekturen. Besteht der Treiber die Prüfung beim Start nicht, das alte",
    "Модель памяти и трансляции":
        "Speicher- und Übersetzungsmodell",
    "Авто: новая на AMD, старая на других":
        "Automatisch: neu auf AMD, alt auf anderen",
    "Новая":
        "Neu",
    "Старая (как в 0.3)":
        "Alt (wie in 0.3)",
    "О программе":
        "Über",
    "Сначала закройте игру":
        "Schließe zuerst das Spiel",
    "Основано на bbport от deadinside28":
        "Basiert auf bbport von deadinside28",
    "Лицензия":
        "Lizenz",
    'GNU GPL v2 или новее · Файлы игры не входят.': 'GNU GPL v2 oder neuer · Keine Spieldateien enthalten.',
    # 0.51: mouse look, choosing NVIDIA's DLSS library, the online module
    'DLSS {}: готово':
        'DLSS {}: bereit',
    'DLSS найден (нужна видеокарта NVIDIA RTX)':
        'DLSS gefunden (benötigt eine NVIDIA-RTX-Grafikkarte)',
    'DLSS не найден: выберите библиотеку NVIDIA ниже (и нужна сборка с мостом DLSS). Игра включит FSR 3.1':
        'DLSS nicht gefunden: Wähle unten die NVIDIA-Bibliothek (außerdem ist ein Build mit der DLSS-Brücke nötig). Das Spiel verwendet FSR 3.1',
    'DLSS: библиотека NVIDIA':
        'DLSS: NVIDIA-Bibliothek',
    '{} — библиотека DLSS для Windows; на Linux NVIDIA её не загружает. Нужна libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        '{} ist die DLSS-Bibliothek für Windows; NVIDIAs Linux-Treiber lädt sie nicht. Benötigt wird libnvidia-ngx-dlss.so.<Version> aus NVIDIAs DLSS SDK: {}',
    'Библиотека DLSS NVIDIA (libnvidia-ngx-dlss.so.*)':
        'NVIDIAs DLSS-Bibliothek (libnvidia-ngx-dlss.so.*)',
    'Выбрать файл…':
        'Datei wählen…',
    'Из сборки: {}':
        'Aus diesem Build: {}',
    'Инвертировать мышь по вертикали':
        'Maus-Y-Achse umkehren',
    'Камера мышью':
        'Kamera mit der Maus',
    'Клавиатура и мышь':
        'Tastatur und Maus',
    'Не удалось прочитать файл':
        'Die Datei konnte nicht gelesen werden',
    'Не удалось скопировать библиотеку':
        'Die Bibliothek konnte nicht kopiert werden',
    'Нет: выберите libnvidia-ngx-dlss.so.* из DLSS SDK NVIDIA ({})':
        'Keine: Wähle libnvidia-ngx-dlss.so.* aus NVIDIAs DLSS SDK ({})',
    'Нужен файл libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}':
        'Benötigt wird libnvidia-ngx-dlss.so.<Version> aus NVIDIAs DLSS SDK: {}',
    'Нужна библиотека для Linux':
        'Eine Linux-Bibliothek wird benötigt',
    'Своя: {}':
        'Eigene: {}',
    'Убрать выбранную':
        'Gewählte entfernen',
    'Чувствительность мыши':
        'Mausempfindlichkeit',
    'Щелчок в окне игры захватывает мышь, F1 — отпускает':
        'Ein Klick ins Spielfenster fängt die Maus, F1 gibt sie frei',
    'Эта сборка без модуля онлайна (libbbnet.so): игра только офлайн':
        'Dieser Build hat kein Online-Modul (libbbnet.so): nur Offline-Spiel',
    'Эта сборка без моста DLSS (libbbport_dlss.so): DLSS работать не будет':
        'Dieser Build hat keine DLSS-Brücke (libbbport_dlss.so): DLSS funktioniert nicht',
    'Это не библиотека DLSS':
        'Das ist nicht die DLSS-Bibliothek',
    # Online page: the server
    'Адрес сервера (host:port)':
        'Serveradresse (Host:Port)',
    'Сервер shadNet':
        'shadNet-Server',
    # Trophies page
    'В дампе игры нет трофеев (sce_sys/trophy)':
        'Der Spiel-Dump hat keine Trophäen (sce_sys/trophy)',
    'Записываются, когда игра их открывает, и показываются в игре':
        'Werden gespeichert, wenn das Spiel sie freischaltet, und im Spiel angezeigt',
    'Ключ трофеев':
        'Trophäen-Schlüssel',
    'Неверный ключ трофеев: названия недоступны':
        'Falscher Trophäen-Schlüssel: die Namen sind nicht verfügbar',
    'Получен {}':
        'Erhalten am {}',
    'Получено {} из {}':
        '{} von {} erhalten',
    'Скрытый трофей':
        'Versteckte Trophäe',
    'Трофеи':
        'Trophäen',
    'Платиновый':
        'Platin',
    'Золотой':
        'Gold',
    'Серебряный':
        'Silber',
    'Бронзовый':
        'Bronze',
    "Вход в shadNet": "shadNet-Anmeldung",
    "неверное имя или пароль": "falscher Name oder falsches Passwort",
    "такой учётной записи нет на этом сервере": "dieses Konto gibt es auf diesem Server nicht",
    "эта учётная запись уже в сети (игра запущена?)": "dieses Konto ist bereits angemeldet (läuft das Spiel?)",
    "вход выполнен": "angemeldet",
    "вход не удался ({})": "Anmeldung fehlgeschlagen ({})",
    # About: Thanks
    'Благодарности': 'Danksagungen',
    'Без них ничего этого не было бы': 'Ohne sie wäre nichts davon möglich',
    'Порт и его код': 'Der Port und sein Code',
    'Помощь и тесты': 'Hilfe und Tests',
    'Другие благодарности': 'Dank auch an',
    'bbport — порт, на котором построен весь этот проект': 'bbport, der Port, auf dem dieses ganze Projekt aufbaut',
    'Игра по сети, DLSS, страница читов, добавление в Steam, значок, пропуск конвейеров, которые драйвер не может создать, и игра без вылета при нехватке видеопамяти': 'Online-Spiel, DLSS, die Cheat-Seite, Zu Steam hinzufügen, das Symbol, das Überspringen von Pipelines, die der Treiber nicht erstellen kann, und kein Absturz bei vollem Videospeicher',
    'Собрал и адаптировал десятки исправлений: вылеты при загрузке, чёрные изображения, апскейлер, строка производительности в журнале': 'Hat Dutzende Korrekturen gesammelt und angepasst: Abstürze beim Laden, schwarze Bilder, der Upscaler, die Leistungszeile im Log',
    'Чёрный предпросмотр персонажа, картинка экрана загрузки и память кэша текстур': 'Die schwarze Charaktervorschau, das Bild des Ladebildschirms und der Speicher des Texturcaches',
    'Кэш текстур вовремя освобождает видеопамять': 'Der Texturcache gibt Videospeicher rechtzeitig frei',
    'Вылеты при загрузке областей': 'Abstürze beim Laden von Gebieten',
    'Интерфейс, пропадавший не в 1080p, векторы движения больших чудовищ и ошибка памяти': 'Die Oberfläche, die außerhalb von 1080p verschwand, Bewegungsvektoren der großen Bestien und ein Speicherfehler',
    'Вылеты при загрузке некоторых карт и меню жестов с клавиатуры': 'Abstürze beim Laden mancher Karten und das Gestenmenü über die Tastatur',
    'Экранная клавиатура для имени персонажа и уведомление о компиляции шейдеров': 'Die Bildschirmtastatur für den Charakternamen und der Hinweis zum Kompilieren der Shader',
    'Сетевые библиотеки игры по сети и сервер для своего кооператива': 'Die Bibliotheken für das Online-Spiel und der Server für den eigenen Koop',
    'Основа поддержки DLSS и модель FSR 4 без шлейфов за персонажами': 'Die Grundlage für DLSS und das FSR-4-Modell ohne Schlieren hinter Figuren',
    'Апскейлер FSR 3.1': 'Der FSR-3.1-Upscaler',
    'Игра запускается, когда DLSS нельзя использовать': 'Das Spiel startet, wenn DLSS nicht nutzbar ist',
    'Перевод на упрощённый китайский': 'Die Übersetzung ins vereinfachte Chinesisch',
    'Звук игры на полной громкости': 'Der Spielton in voller Lautstärke',
    'Флажки и ползунки внутриигрового меню': 'Die Kontrollkästchen und Schieberegler des Spielmenüs',
    'Подробные отчёты с журналами и проверка исправлений': 'Ausführliche Berichte mit Logs und Tests der Korrekturen',
    'Идея поменять местами A и B на контроллерах в стиле Nintendo': 'Die Idee, A und B bei Controllern im Nintendo-Stil zu tauschen',
    'Проверка исправления видеопамяти': 'Test der Videospeicher-Korrektur',
    'Рендерер и компилятор шейдеров': 'Der Renderer und der Shader-Recompiler',
    'Инструмент для сборки AppImage': 'Das Werkzeug, das das AppImage baut',
    'Нашёл ошибку, из-за которой игра не запускалась на некоторых видеокартах, и ускорение камеры на DualShock 4': 'Hat den Fehler gefunden, der den Spielstart auf manchen Grafikkarten verhinderte, und die beschleunigte Kamera am DualShock 4',
    'Нашёл, почему игра не запускалась в игровом режиме Steam Deck': 'Hat herausgefunden, warum das Spiel im Spielmodus des Steam Deck nicht startete',
    'Нашёл, при каких эффектах зависают загрузки на NVIDIA': 'Hat herausgefunden, welche Effekte Ladebildschirme auf NVIDIA einfrieren',
    'ps4-pkg-extractor: установка игры из файлов .pkg': 'ps4-pkg-extractor: das Spiel aus .pkg-Dateien installieren',
    # Shader cache
    'Кэш шейдеров': 'Shader-Cache',
    'Очистить': 'Leeren',
    '{}. Если после обновления картинка выглядит странно, очистите его: шейдеры соберутся заново (первые минуты в каждой зоне возможны рывки)': '{}. Wenn das Bild nach einem Update seltsam aussieht, leeren: Die Shader werden neu erstellt (in den ersten Minuten jedes Gebiets kann es ruckeln)',
    'Пусто: шейдеры соберутся при игре': 'Leer: Die Shader werden beim Spielen erstellt',
    'Очистить кэш шейдеров?': 'Shader-Cache leeren?',
    'Игра соберёт шейдеры заново: первые минуты в каждой зоне возможны рывки. Сохранения и настройки не затрагиваются.': 'Das Spiel erstellt die Shader neu: In den ersten Minuten jedes Gebiets kann es ruckeln. Spielstände und Einstellungen bleiben unberührt.',
    'Названия трофеев на английском без ключа и звук при получении трофея': 'Trophäennamen auf Englisch ohne Schlüssel und der Ton beim Erhalt einer Trophäe',
    'Буфер трафарета, в который писали цветные изображения': 'Der Stencil-Puffer, in den Farbbilder schrieben',
    'Вход на публичный сервер shadNet без отключения': 'Auf dem öffentlichen shadNet-Server angemeldet bleiben',
    'Установить из PKG': 'Aus PKG installieren',
    'Выбрать .pkg…': '.pkg auswählen…',
    'Файлы .pkg: игра, обновление, DLC': '.pkg-Dateien: Spiel, Update, DLC',
    'Куда установить игру': 'Wohin das Spiel installieren',
    'Установка…': 'Installiere…',
    'Игра установлена: {}': 'Spiel installiert: {}',
    'Не удалось установить: подробности в журнале': 'Installation fehlgeschlagen: Details im Protokoll',
    'Выход из игры из меню с контроллера, меню в пределах экрана и половины тачпада на Xbox': 'Das Spiel im Menü mit dem Controller beenden, das Menü innerhalb des Bildschirms und die Touchpad-Hälften auf Xbox-Controllern',
    'Вылет видеоплеера при его остановке': 'Ein Absturz des Videoplayers beim Anhalten',
    'Язык внутриигрового меню при запуске без окна лаунчера': 'Die Sprache des Spielmenüs beim Start ohne Launcher-Fenster',
    'DLSS в AppImage на NVIDIA': 'DLSS im AppImage auf NVIDIA',
    'Сверхширокие мониторы без растянутой картинки': 'Ultrawide-Monitore ohne gestrecktes Bild',
    'Движение с клавиатуры: круглая диагональ и последняя нажатая клавиша': 'Bewegung per Tastatur: runde Diagonale und die zuletzt gedrückte Taste',
    'Отладка вылетов: процесс ждёт отладчик (BB_FAULT_WAIT)': 'Absturz-Debugging: Der Prozess wartet auf einen Debugger (BB_FAULT_WAIT)',
    'Видеопамять на картах с 4 ГБ и вылеты: флипы, swapchain, дескрипторы и ошибки страниц; смена стиков и инверсия камеры, импорт сохранений, выбор версии': 'Videospeicher auf 4-GB-Karten und Abstürze: Flips, Swapchain, Deskriptoren und Seitenfehler; Sticks tauschen und Kamera invertieren, Spielstände importieren, Versionsauswahl',
    'Большие группы команд записи и swapchain после изменений экрана': 'Große aufgezeichnete Befehlsgruppen und die Swapchain nach Anzeigeänderungen',
    # GODZILLA (gzport)
    'GODZILLA {}, версия 1.01':
        'GODZILLA {}, Version 1.01',
    'GODZILLA добавлена в библиотеку Steam':
        'GODZILLA wurde zur Steam-Bibliothek hinzugefügt',
    'GODZILLA — товарный знак Toho Co., Ltd.; игра для PS4 издана Bandai Namco Entertainment. Этот проект с ними не связан.':
        'GODZILLA ist eine Marke der Toho Co., Ltd.; das PS4-Spiel wurde von Bandai Namco Entertainment veröffentlicht. Dieses Projekt steht in keiner Verbindung zu ihnen.',
    'XML-патчи в формате shadPS4 для версии 01.01 из папки патчей. Применяются при запуске.':
        'XML-Patches im shadPS4-Format für Version 01.01 aus dem Patches-Ordner. Werden beim Start angewendet.',
    'eboot.bin не от версии 1.01: скопируйте eboot.bin из дампа обновления 1.01 в папку игры с заменой':
        'Die eboot.bin ist nicht von 1.01: Kopiere die eboot.bin aus dem extrahierten Update 1.01 in den Spielordner und ersetze sie',
    'gzport — нативный порт для Linux':
        'gzport — nativer Linux-Port',
    'Авторы bbport и bloodborne_linux, на которых построен gzport, и все, кто им помогал':
        'Die Autoren von bbport und bloodborne_linux, auf denen gzport aufbaut, und alle, die ihnen geholfen haben',
    'В папке игры нет: {}. Распакуйте игру и обновление 1.01 заново':
        'Im Spielordner fehlt: {}. Entpacke das Spiel und das Update 1.01 erneut',
    'В этой папке нет сохранений GODZILLA (SAVEDATA00 с DATA.BIN)':
        'Keine GODZILLA-Spielstände in diesem Ordner (SAVEDATA00 mit DATA.BIN)',
    'Игра идёт с 60 FPS, как на PS4. Выше 60 FPS: нужен патч частоты кадров, его пока нет':
        'Das Spiel läuft mit 60 FPS wie auf der PS4. Mehr als 60 FPS braucht einen Bildraten-Patch, der noch nicht verfügbar ist',
    'Для GODZILLA пока недоступен: игра рисует кадр прямо в разрешении вывода':
        'Für GODZILLA noch nicht verfügbar: das Spiel zeichnet das Bild direkt in der Ausgabeauflösung',
    'Игра, обновление 1.01 и DLC из ваших файлов .pkg':
        'Das Spiel, Update 1.01 und DLC aus Ihren .pkg-Dateien',
    'Ключ трофеев PS4 (TrophyKey в shadPS4), 32 шестнадцатеричных символа: с ним названия и описания на языке игры. Хранится на этом компьютере. Без него видны только значки':
        'Der Trophäen-Schlüssel der PS4 (TrophyKey in shadPS4), 32 Hexadezimalziffern: damit sind Namen und Beschreibungen in der Sprache des Spiels. Bleibt auf diesem Computer. Ohne ihn sind nur die Symbole zu sehen',
    'Нативный порт для Linux, версия {}':
        'Nativer Linux-Port, Version {}',
    'Нужен патч для версии 1.01, его пока нет':
        'Braucht einen Patch für Version 1.01, noch nicht verfügbar',
    'Нужно обновление 1.01: скопируйте файлы дампа обновления 1.01 в папку игры с заменой (найдена версия {})':
        'Das Update 1.01 wird benötigt: Kopiere das extrahierte Update 1.01 in den Spielordner und ersetze dabei die Dateien (gefundene Version {})',
    'Основано на bloodborne_linux от ayozetr':
        'Basiert auf bloodborne_linux von ayozetr',
    'bloodborne_linux: порт для Linux, на котором построен gzport':
        'bloodborne_linux: der Linux-Port, auf dem gzport aufbaut',
    'Папка с сохранениями GODZILLA':
        'Ordner mit GODZILLA-Spielständen',
    'Патчи игры':
        'Spiel-Patches',
    'Португальский (Бразилия)':
        'Portugiesisch (Brasilien)',
    'Это не GODZILLA (найдено {}): нужна GODZILLA (CUSA02046) с обновлением 1.01':
        'Das ist nicht GODZILLA (gefunden: {}): Benötigt wird GODZILLA (CUSA02046) mit Update 1.01',
    'Тачпад, левая половина':
        'Touchpad, linke Hälfte',
    'Тачпад, правая половина':
        'Touchpad, rechte Hälfte',
    'Настройки по умолчанию':
        'Standardwerte',
    'Восстановить мои настройки по умолчанию':
        'Meine Standardwerte wiederherstellen',
    'Вернуть':
        'Wiederherstellen',
    'Сохранить текущие как мои настройки по умолчанию':
        'Aktuelle als meine Standardwerte speichern',
    'Настройки лаунчера и bbport.ini, без назначений кнопок':
        'Einstellungen des Launchers und der bbport.ini, ohne Tastenbelegungen',
    'Сохранить':
        'Speichern',
    'Из {}':
        'Aus {}',
    'Своих настроек по умолчанию пока нет: восстанавливаются встроенные (папки и ключ трофеев не меняются)':
        'Noch keine eigenen Standardwerte: die eingebauten werden wiederhergestellt (Ordner und Trophäenschlüssel bleiben)',
    'Не удалось прочитать {}':
        '{} konnte nicht gelesen werden',
    'Восстановить настройки по умолчанию?':
        'Standardwerte wiederherstellen?',
    'Настройки лаунчера и bbport.ini станут такими, как в {}. Остальные строки bbport.ini, в том числе назначения кнопок, не меняются':
        'Die Einstellungen des Launchers und der bbport.ini werden zu denen aus {}. Die übrigen Zeilen der bbport.ini, Tastenbelegungen eingeschlossen, bleiben unverändert',
    'Своих настроек по умолчанию нет: настройки лаунчера и bbport.ini станут встроенными. Папки, ключ трофеев и назначения кнопок не меняются':
        'Keine eigenen Standardwerte: die Einstellungen des Launchers und der bbport.ini werden auf die eingebauten gesetzt. Ordner, Trophäenschlüssel und Tastenbelegungen bleiben unverändert',
    'Настройки по умолчанию восстановлены':
        'Standardwerte wiederhergestellt',
    'Сохранить текущие настройки как свои по умолчанию?':
        'Aktuelle Einstellungen als Ihre Standardwerte speichern?',
    'Они запишутся в {} вместо прежних, и «Вернуть» будет восстанавливать их':
        'Sie werden in {} anstelle der bisherigen gespeichert, und „Wiederherstellen“ kehrt zu ihnen zurück',
    'Не удалось сохранить {}':
        '{} konnte nicht gespeichert werden',
    'Текущие настройки сохранены как ваши по умолчанию':
        'Aktuelle Einstellungen als Ihre Standardwerte gespeichert',
    # Online page (LAN versus)
    "Версус по локальной сети: VS MODE в меню «Онлайн» игры, через ваш сервер shadNet (shadnet-p2p с патчем gzport). У каждого игрока своя учётная запись на этом сервере": "Versus im lokalen Netzwerk: VS MODE im „Online“-Menü des Spiels, über deinen eigenen shadNet-Server (shadnet-p2p mit dem gzport-Patch). Jeder Spieler hat ein eigenes Konto auf diesem Server",
    "Как настроить версус по сети": "Versus im Netzwerk einrichten",
    "Имя учётной записи на сервере shadNet (оно же ваше имя в игре) и её пароль. Пароль хранится на этом компьютере вместе с настройками лаунчера": "Dein Kontoname auf dem shadNet-Server (zugleich dein Name im Spiel) und sein Passwort. Das Passwort wird auf diesem Computer mit den Launcher-Einstellungen gespeichert",
    "Порт P2P (UDP)": "P2P-Port (UDP)",
    "Через него игроки соединяются напрямую; он должен быть открыт между компьютерами": "Darüber verbinden sich die Spieler direkt; er muss zwischen den Computern offen sein",
    "Укажите адрес сервера": "Gib die Serveradresse ein",
    "UDP сервера shadNet": "UDP des shadNet-Servers",
    "отвечает; сервер видит этот компьютер как {}": "antwortet; der Server sieht diesen Computer als {}",
    "не отвечает: матч не соединится": "keine Antwort: das Match wird sich nicht verbinden",
}


# Simplified Chinese.
ZH_CN = {
    # Window, pages, buttons
    "Запустить": "启动",
    "Остановить": "停止",
    "Настройки": "设置",
    "Журнал": "日志",
    "Не удалось запустить: {}": "无法启动：{}",
    "\n— игра завершилась (код {}) —\n": "\n— 游戏已退出（代码 {}）—\n",
    # Launcher language
    "Язык лаунчера": "启动器语言",
    "Как в системе": "跟随系统",
    "Применится после перезапуска лаунчера, пока игра запущена":
        "游戏运行期间更改语言，需要重启启动器后才会生效",
    # Game
    "Игра": "游戏",
    "Папка игры ({})": "游戏文件夹（{}）",
    "Папка игры": "游戏文件夹",
    "Выбрать папку с eboot.bin": "选择包含 eboot.bin 的文件夹",
    "Открыть в файловом менеджере": "在文件管理器中打开",
    "Папка сохранений": "存档文件夹",
    "Выбрать папку сохранений": "选择存档文件夹",
    "Вернуть папку по умолчанию": "恢复默认文件夹",
    "Язык системы": "系统语言",
    "По умолчанию: {}": "默认：{}",
    "Найдены сохранения": "已找到存档",
    "Сохранений пока нет: игра создаст их здесь": "暂无存档：游戏会在此创建",
    "не выбрана": "未选择",
    "Нет eboot.bin в папке": "文件夹中没有 eboot.bin",
    "Управление": "操作设置",
    "Геймпад": "手柄",
    "Назначение кнопок; применяется при запуске игры": "按键绑定；在游戏启动时生效",
    "Назначить": "绑定",
    "Сбросить": "重置",
    "{} (по умолчанию)": "{}（默认）",
    "не назначено": "未绑定",
    "Нажмите клавишу или кнопку… (Esc — отмена)": "按下一个按键或手柄按钮…（按 Esc 取消）",
    "Крест": "叉键",
    "Круг": "圆圈键",
    "Квадрат": "方块键",
    "Треугольник": "三角键",
    "Крестовина вверх": "方向键上",
    "Крестовина вниз": "方向键下",
    "Крестовина влево": "方向键左",
    "Крестовина вправо": "方向键右",
    "Движение вперёд": "向前移动",
    "Движение назад": "向后移动",
    "Движение влево": "向左移动",
    "Движение вправо": "向右移动",
    "Камера вверх": "镜头向上",
    "Камера вниз": "镜头向下",
    "Камера влево": "镜头向左",
    "Камера вправо": "镜头向右",
    "Контроллер": "控制器",
    "Выбранный берётся, как только подключится": "所选手柄一旦连接即会被使用",
    "Первый подключённый": "第一个已连接的手柄",
    "{} (не подключён)": "{}（未连接）",
    "eboot.bin не читается как расшифрованный исполняемый файл PS4: сделайте дамп заново":
        "无法将 eboot.bin 识别为已解密的 PS4 可执行文件：请重新转储游戏",
    "Папка игры (с eboot.bin)": "游戏文件夹（含 eboot.bin）",
    # Languages
    "Английский": "英语",
    "Русский": "俄语",
    "Французский": "法语",
    "Испанский": "西班牙语",
    "English": "英语",
    # Mods
    "Обновить список": "刷新列表",
    # Patches
    "Сторонние патчи": "第三方补丁",
    "Папка патчей": "补丁文件夹",
    "Выбрать папку патчей": "选择补丁文件夹",
    "Открыть папку патчей": "打开补丁文件夹",
    "Патчей нет": "没有补丁",
    "Автор: {}": "作者：{}",
    # Screen
    "Экран": "显示",
    "Разрешение вывода": "输出分辨率",
    "Апскейлер дорисовывает кадр; Steam Deck — 720p": "超分辨率会将画面放大到此分辨率；Steam Deck 建议 720p",
    "Полноэкранный режим": "全屏模式",
    "Смена разрешения на лету": "实时切换分辨率",
    "Без перезапуска, но медленнее на Steam Deck и старых GPU":
        "无需重启，但在 Steam Deck 和较旧的显卡上速度更慢",
    "Авто (по видеокарте)": "自动（根据显卡）",
    "Выключена (быстрее)": "关闭（更快）",
    "Включена": "开启",
    "Режим показа кадров": "呈现模式",
    "Разрешить HDR": "允许 HDR",
    # Upscaler
    "Апскейлер": "超分辨率",
    "Хранится в bbport.ini; в игре меняется через меню (Insert или L3+R3)":
        "保存在 bbport.ini 中；游戏内可通过菜单切换（Insert 或 L3+R3）",
    "TAA (нативное сглаживание)": "TAA（原生抗锯齿）",
    "Выключен": "关闭",
    "Пресет": "预设",
    "Резкость (RCAS)": "锐化（RCAS）",
    "Сила резкости": "锐化强度",
    "Векторы движения объектов": "物体运动矢量",
    "Меньше гостинга на персонажах; стоит около 10% FPS": "减少角色拖影；大约损失 10% 帧率",
    "Показывать FPS": "显示帧率",
    "Ассеты найдены": "已找到资源文件",
    "Нет ассетов: tools/fetch_fsr4_assets.sh": "缺少资源文件：请运行 tools/fetch_fsr4_assets.sh",
    "Ассеты для выбранного режима найдены": "已找到所选模式对应的资源文件",
    "{}. Соберите FSR 4.1.1 из своей DLL кнопкой «Выбрать DLL…» ниже":
        "{}。请用下方的「选择 DLL…」按钮，从你自己的 DLL 构建 FSR 4.1.1",
    "FSR 4.1.1 из своей DLL AMD": "用你自己的 AMD DLL 构建 FSR 4.1.1",
    "Отменить": "取消",
    "Выбрать DLL…": "选择 DLL…",
    "DLL апскейлера AMD (amd_fidelityfx_upscaler_dx12.dll)": "AMD 超分辨率 DLL（amd_fidelityfx_upscaler_dx12.dll）",
    "нет": "无",
    "Эта DLL не подходит": "此 DLL 不适用",
    "{}: версия {}, модели FSR 4: {}.\n\nbbport повторяет только официальную FSR 4.1.x от AMD (модель v07_fp8_no_scale): например, FSR4_LATEST из OptiScaler или amd_fidelityfx_upscaler_dx12.dll из игры с FSR 4.1. Сборки сообщества (4.0.2b и подобные) устроены иначе и пока не поддерживаются.":
        "{}：版本 {}，FSR 4 模型：{}。\n\nbbport 仅支持复现 AMD 官方的 FSR 4.1.x（v07_fp8_no_scale 模型）：例如 OptiScaler 中的 FSR4_LATEST，或来自支持 FSR 4.1 的游戏的 amd_fidelityfx_upscaler_dx12.dll。社区构建版本（如 4.0.2b 等）结构不同，暂不支持。",
    "Загрузчик не подходит": "此加载器不适用",
    "Загрузчик FidelityFX (amd_fidelityfx_loader_dx12.dll или amd_fidelityfx_dx12.dll)":
        "FidelityFX 加载器（amd_fidelityfx_loader_dx12.dll 或 amd_fidelityfx_dx12.dll）",
    "\n— сборка FSR 4.1.1 из {} —\n": "\n— 正在从 {} 构建 FSR 4.1.1 —\n",
    "Подготовка…": "准备中…",
    "Запись проходов DLL под Proton: {} из {}": "正在 Proton 下录制 DLL 渲染通道：{} / {}",
    "Перевод проходов в SPIR-V…": "正在将渲染通道转换为 SPIR-V…",
    "— сборка FSR 4.1.1 завершилась (код {}) —\n": "— FSR 4.1.1 构建已完成（代码 {}）—\n",
    "FSR 4.1.1 собран и выбран": "FSR 4.1.1 已构建并选用",
    "Сборка FSR 4.1.1 отменена": "FSR 4.1.1 构建已取消",
    "FSR 4.1.1 не собран": "FSR 4.1.1 尚未构建",
    "DLL не подходит: подробности в журнале": "DLL 不适用：详情见日志",
    "Не хватает программ для сборки: список в журнале": "缺少构建所需的程序：清单见日志",
    "Записанные проходы не совпали с тем, что повторяет bbport (другая версия DLL или новая видеокарта?): подробности в журнале":
        "录制的渲染通道与 bbport 复现的内容不一致（可能是 DLL 版本不同，或显卡型号较新？）：详情见日志",
    "Не найден загрузчик FidelityFX 2.x": "未找到 FidelityFX 2.x 加载器",
    "Не найден подходящий Proton: установите GE-Proton 10 или новее (ProtonUp-Qt) или Proton Experimental / Proton-CachyOS в Steam. Если они есть — запустите в Steam любую игру с этим Proton, чтобы Steam поставил его рантайм":
        "未找到合适的 Proton：请安装 GE-Proton 10 或更高版本（可用 ProtonUp-Qt），或在 Steam 中使用 Proton Experimental / Proton-CachyOS。如果已经安装，请在 Steam 中用该 Proton 启动任意游戏，让 Steam 安装它的运行时",
    "Ни один Proton не запустил FSR 4.1 из этой DLL. Либо они слишком старые (подходят GE-Proton 10+, Proton Experimental, Proton-CachyOS 11), либо DLL не включает FSR 4.1 на этой видеокарте (Steam Deck?): тогда соберите на ПК с Radeon RX 7000/9000 и скопируйте папку fsr4_411. Подробности в журнале":
        "没有任何 Proton 能从此 DLL 启动 FSR 4.1。要么是 Proton 版本太旧（需要 GE-Proton 10+、Proton Experimental 或 Proton-CachyOS 11），要么是这块显卡无法启用 FSR 4.1（例如 Steam Deck？）：这种情况下，请在装有 Radeon RX 7000/9000 的电脑上构建，再把 fsr4_411 文件夹复制过来。详情见日志",
    "На NixOS запись идёт на самой системе (systemd --user) через umu-launcher из nix-shell, а здесь их не нашлось: установите umu-launcher или Nix. Подробности в журнале":
        "在 NixOS 上，录制通过 nix-shell 中的 umu-launcher 在系统本身（systemd --user）上进行，但未能找到它们：请安装 umu-launcher 或 Nix。详情见日志",
    "{}: FSR {}. Это официальная FSR 4.0.x от AMD: она включается только на видеокартах RDNA4 (RX 9000), а под Proton на других видеокартах не запускается, поэтому записать её нельзя.\n\nНужна FSR 4.1.x: например, FSR4_LATEST из OptiScaler или DLL из игры с FSR 4.1.":
        "{}：FSR {}。这是 AMD 官方的 FSR 4.0.x：仅在 RDNA4 显卡（RX 9000）上启用，在其他显卡上通过 Proton 无法运行，因此无法录制。\n\n需要 FSR 4.1.x：例如 OptiScaler 中的 FSR4_LATEST，或来自支持 FSR 4.1 的游戏的 DLL。",
    "{}: в этой DLL нет FSR 4. Нужна amd_fidelityfx_upscaler_dx12.dll версии 4.1.x.":
        "{}：此 DLL 中不包含 FSR 4。需要版本为 4.1.x 的 amd_fidelityfx_upscaler_dx12.dll。",
    "Это не загрузчик":
        "这不是加载器",
    "{} — это DLL апскейлера. Загрузчик называется amd_fidelityfx_loader_dx12.dll (у OptiScaler — amd_fidelityfx_dx12.dll) и лежит в той же папке игры, что и DLL апскейлера.":
        "{} 是超分辨率 DLL。加载器名为 amd_fidelityfx_loader_dx12.dll（在 OptiScaler 中为 amd_fidelityfx_dx12.dll），与超分辨率 DLL 位于同一个游戏文件夹中。",
    "{}: версия {}. Нужен загрузчик FidelityFX 2.x — из той же игры, что и DLL апскейлера.":
        "{}：版本 {}。需要来自同一游戏、与超分辨率 DLL 配套的 FidelityFX 2.x 加载器。",
    "Рядом с DLL нет загрузчика: выберите amd_fidelityfx_loader_dx12.dll из папки игры":
        "DLL 旁边没有加载器：请从游戏文件夹中选择 amd_fidelityfx_loader_dx12.dll",
    "Собрать FSR 4.1.1 из amd_fidelityfx_upscaler_dx12.dll 4.1.x (OptiScaler: папка FSR4_LATEST, или из игры с FSR 4.1). Нужен GE-Proton 10+, Proton Experimental или Proton-CachyOS; 2–5 минут (RDNA4: вдвое дольше, ещё и вариант FP8)":
        "从 amd_fidelityfx_upscaler_dx12.dll 4.1.x 构建 FSR 4.1.1（OptiScaler：FSR4_LATEST 文件夹，或来自支持 FSR 4.1 的游戏）。需要 GE-Proton 10+、Proton Experimental 或 Proton-CachyOS；耗时 2–5 分钟（RDNA4：耗时加倍，并额外构建 FP8 版本）",
    "Сборка не удалась (код {}): подробности в журнале": "构建失败（代码 {}）：详情见日志",
    "Сглаживание в разрешении вывода без модели FSR": "在输出分辨率下进行抗锯齿，不使用 FSR 模型",
    "DLSS найден (нужна видеокарта NVIDIA RTX)": "已找到 DLSS（需要 NVIDIA RTX 显卡）",
    "DLSS: библиотека NVIDIA": "DLSS：NVIDIA 库",
    "Выбрать файл…": "选择文件…",
    "Убрать выбранную": "移除所选",
    "Своя: {}": "自定义：{}",
    "Из сборки: {}": "随版本附带：{}",
    "Нет: выберите libnvidia-ngx-dlss.so.* из DLSS SDK NVIDIA ({})": "无：请选择 NVIDIA DLSS SDK 中的 libnvidia-ngx-dlss.so.*（{}）",
    "Эта сборка без моста DLSS (libbbport_dlss.so): DLSS работать не будет": "此版本没有 DLSS 桥接（libbbport_dlss.so）：DLSS 无法工作",
    "Библиотека DLSS NVIDIA (libnvidia-ngx-dlss.so.*)": "NVIDIA DLSS 库（libnvidia-ngx-dlss.so.*）",
    "Нужна библиотека для Linux": "需要 Linux 版本的库",
    "{} — библиотека DLSS для Windows; на Linux NVIDIA её не загружает. Нужна libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}":
        "{} 是 Windows 版 DLSS 库，NVIDIA 的 Linux 驱动不会加载它。需要 NVIDIA DLSS SDK 中的 libnvidia-ngx-dlss.so.<版本>：{}",
    "Не удалось прочитать файл": "无法读取文件",
    "Это не библиотека DLSS": "这不是 DLSS 库",
    "Нужен файл libnvidia-ngx-dlss.so.<версия> из DLSS SDK NVIDIA: {}": "需要 NVIDIA DLSS SDK 中的 libnvidia-ngx-dlss.so.<版本>：{}",
    "Не удалось скопировать библиотеку": "无法复制该库",
    "DLSS {}: готово": "DLSS {}：已就绪",
    "Клавиатура и мышь": "键盘和鼠标",
    "Камера мышью": "鼠标控制视角",
    "Щелчок в окне игры захватывает мышь, F1 — отпускает": "在游戏窗口中单击以捕获鼠标，按 F1 释放",
    "Чувствительность мыши": "鼠标灵敏度",
    "Инвертировать мышь по вертикали": "反转鼠标纵轴",
    "DLSS не найден: выберите библиотеку NVIDIA ниже (и нужна сборка с мостом DLSS). Игра включит FSR 3.1":
        "未找到 DLSS：请在下方选择 NVIDIA 的库（还需要带 DLSS 桥接的版本）。游戏将改用 FSR 3.1",
    "Нет или повреждён файл {}": "文件 {} 缺失或已损坏",
    # Effects
    "Пропуск заставок при запуске": "跳过开场动画",
    # Frame rate
    "Частота кадров": "帧率",
    "Режим": "模式",
    "Какой патч частоты кадров применить к игре": "对游戏应用哪种帧率补丁",
    "Без ограничения (патч)": "不限制（补丁解锁）",
    "60 (как на PS4)": "60（与 PS4 一致）",
    "Ограничение FPS": "帧率上限",
    "0 — без ограничения; укажите число, чтобы ограничить FPS":
        "0 表示不限制；填写一个数字可限制帧率",
    # Performance
    "Производительность": "性能",
    "Двухстадийный конвейер GPU": "双阶段 GPU 管线",
    "Быстрее на 20–30%; при нестабильности выключите": "可提速 20–30%；如不稳定请关闭",
    "Авто": "自动",
    "Включён при 8 и более потоках процессора": "处理器有 8 个或以上线程时自动开启",
    "Включён": "开启",
    "Стабильнее, но медленнее": "更稳定，但速度更慢",
    "Чтение данных GPU процессором": "由 CPU 读取 GPU 数据（readback）",
    "По умолчанию": "默认",
    "Фоновая загрузка в видеопамять": "后台预加载至显存",
    "Меньше рывков при подгрузке зон": "区域加载时卡顿更少",
    "Обычная": "普通",
    "Без лишней видеопамяти": "不占用额外显存",
    "Полная": "完整",
    "Около 3 ГБ видеопамяти сверху": "额外占用约 3 GB 显存",
    # Mode
    "Режим работы": "工作模式",
    "Новая: видеокарта работает с памятью игры напрямую, как в игре для ПК, а команды графики переводятся, а не эмулируются. Старая — модель памяти 0.3 со всеми исправлениями. Если драйвер не проходит проверку при запуске — старая":
        "新模型：显卡像 PC 游戏那样直接读写游戏内存，图形指令被转译而非模拟。旧模型：0.3 版的内存模型，包含所有修复。如果驱动未通过启动检查，则使用旧模型",
    "Модель памяти и трансляции": "内存与指令转译模型",
    "Авто: новая на AMD, старая на других": "自动：AMD 用新模型，其他显卡用旧模型",
    "Новая": "新模型",
    "Старая (как в 0.3)": "旧模型（与 0.3 版相同）",
    "Синхронизация как в 0.3": "与 0.3 版相同的同步方式",
    "Для поиска регрессий: старая модель памяти и ожидания копий как в релизе 0.3":
        "用于排查回归问题：采用与 0.3 版发布时相同的旧内存模型与复制等待方式",
    "Выключена": "关闭",
    "Выключены": "关闭",
    # Developer
    "Для разработчика": "开发者选项",
    "Статистика кадров в журнале": "在日志中记录帧统计",
    "Сохранять журнал и статистику в файл": "将日志和统计信息保存到文件",
    "Диагностика вылетов": "崩溃诊断",
    "Проверяет кучу игры и записывает записи в её память; немного медленнее":
        "检查游戏堆内存并记录对其的写入操作；速度会略有下降",
    "В папку logs в каталоге данных: для разбора рывков и вылетов":
        "保存到数据目录下的 logs 文件夹：便于排查卡顿和崩溃问题",
    "Профиль GPU в журнале": "在日志中记录 GPU 性能剖析",
    "Слои валидации Vulkan": "Vulkan 验证层",
    "Сильно замедляет": "会大幅降低速度",
    "Доп. переменные (ИМЯ=значение через пробел)": "附加环境变量（用空格分隔的 名称=值）",
    # Add to Steam with Flathub's Steam
    'Steam из Flatpak запускает игры в своей песочнице, где нет ни папки игры, ни драйверов: ярлык должен запускать игру вне её (flatpak-spawn --host). Для этого Steam нужно право org.freedesktop.Flatpak, с которым он может запускать программы в вашей системе. Выдать его?':
        'Flatpak 版 Steam 在其沙盒中运行游戏，沙盒里既没有游戏文件夹也没有驱动：快捷方式需要在沙盒外启动游戏（flatpak-spawn --host）。为此 Steam 需要 org.freedesktop.Flatpak 权限，该权限允许它在你的系统上启动程序。是否授予？',
    'Выдать право':
        '授予权限',
    'Не удалось выдать право Steam: {}':
        '无法为 Steam 授予权限：{}',
    "О программе":
        "关于",
    "Сначала закройте игру":
        "请先关闭游戏",
    "Основано на bbport от deadinside28":
        "基于 deadinside28 的 bbport",
    "Лицензия":
        "许可证",
    'GNU GPL v2 или новее · Файлы игры не входят.': 'GNU GPL v2 或更高版本 · 不含游戏文件。',
    # Texts added after the upstream translation
    ", основной": "，主显示器",
    "Steam не закрылся. Закройте его сами и попробуйте ещё раз": "Steam 没有关闭。请手动关闭后重试",
    "Steam не найден (или в него ещё никто не входил)": "未找到 Steam（或尚无人登录过）",
    "Адрес сервера (host:port)": "服务器地址（主机:端口）",
    "В дампе игры нет трофеев (sce_sys/trophy)": "游戏转储中没有奖杯（sce_sys/trophy）",
    "Выбрать папку DLC": "选择 DLC 文件夹",
    "Выключено: игра остаётся офлайн, как раньше": "关闭：游戏和以前一样保持离线",
    "Добавить": "添加",
    "Добавить в Steam": "添加到 Steam",
    "Журнал скопирован": "日志已复制",
    "Журнал сохранён: {}": "日志已保存：{}",
    "Закройте Steam и нажмите «Добавить» ещё раз": "请关闭 Steam 后再次点击“添加”",
    "Закрыть Steam": "关闭 Steam",
    "Записываются, когда игра их открывает, и показываются в игре": "游戏解锁奖杯时记录，并在游戏中显示",
    "Игра в библиотеке Steam запускается сразу, с настройками этого лаунчера": "从 Steam 库启动时会直接进入游戏，并使用本启动器的设置",
    "Играть онлайн": "在线游玩",
    "Поменять местами A и B": "交换 A 和 B",
    "Для контроллеров в стиле Nintendo: подтверждение на A, отмена на B. Применяется при запуске игры": "适用于任天堂风格的手柄：A 确认，B 返回。启动游戏时生效",
    "Ключ трофеев": "奖杯密钥",
    "Копировать": "复制",
    "Поменять стики местами": "交换左右摇杆",
    "Инвертировать камеру геймпада по горизонтали": "手柄视角水平反转",
    "Инвертировать камеру геймпада по вертикали": "手柄视角垂直反转",
    "Импортировать сохранения…": "导入存档…",
    "Импорт сохранений": "导入存档",
    "Это копия с PS4 на флешке (sdimg_*): она зашифрована ключами консоли. Экспортируйте сохранение без шифрования на PS4 (Apollo Save Tool) или через Save Wizard": "这是 PS4 导出到 U 盘的副本（sdimg_*）：它用主机的密钥加密。请在 PS4 上（Apollo Save Tool）或用 Save Wizard 导出未加密的存档",
    "Импортировать сохранения?": "导入存档？",
    "Из {} (изменены {}). Текущие сохранения сначала копируются в {}": "来自 {}（修改于 {}）。当前存档会先复制到 {}",
    "Импортировать": "导入",
    "Не удалось импортировать сохранения": "无法导入存档",
    "Сохранения импортированы": "存档已导入",
    "Монитор": "显示器",
    "Найдено DLC: {}": "找到的 DLC：{}",
    "Не использовать DLC": "不使用 DLC",
    "Не используется": "未使用",
    "Не удалось добавить игру в Steam: {}": "无法将游戏添加到 Steam：{}",
    "Не удалось сохранить журнал: {}": "无法保存日志：{}",
    "Неверный ключ трофеев: названия недоступны": "奖杯密钥错误：无法显示名称",
    "Нет DLC этой игры в папке": "该文件夹中没有本游戏的 DLC",
    "Онлайн": "联机",
    "Основной": "主显示器",
    "Отмена": "取消",
    "Папка DLC": "DLC 文件夹",
    "Пароль": "密码",
    "Пока игра добавляется, Steam нужно закрыть; потом он запустится снова. Закрыть Steam?": "添加游戏时需要关闭 Steam，完成后会重新启动。要关闭 Steam 吗？",
    "Получен {}": "获得于 {}",
    "Получено {} из {}": "已获得 {} / {}",
    "Применяется при запуске игры": "在游戏启动时生效",
    "Проверить": "检测",
    "Проверить соединение": "检测连接",
    "Проверка…": "检测中…",
    "Сервер shadNet": "shadNet 服务器",
    "Скрытый трофей": "隐藏奖杯",
    "Соединение": "连接",
    "Трофеи": "奖杯",
    "Учётная запись": "账号",
    "Экспорт журнала": "导出日志",
    "Экспорт журнала…": "导出日志…",
    "Эта сборка без модуля онлайна (libbbnet.so): игра только офлайн": "此版本没有联机模块（libbbnet.so）：只能离线游玩",
    "доступен": "可连接",
    "недоступен": "无法连接",
    "Вход в shadNet": "shadNet 登录",
    "неверное имя или пароль": "用户名或密码错误",
    "такой учётной записи нет на этом сервере": "此服务器上没有该账户",
    "эта учётная запись уже в сети (игра запущена?)": "该账户已经登录（游戏正在运行吗？）",
    "вход выполнен": "已登录",
    "вход не удался ({})": "登录失败（{}）",
    # About: Thanks
    'Благодарности': '致谢',
    'Без них ничего этого не было бы': '没有他们，这一切都不可能实现',
    'Порт и его код': '移植及其代码',
    'Помощь и тесты': '帮助与测试',
    'Другие благодарности': '同样感谢',
    'bbport — порт, на котором построен весь этот проект': 'bbport，整个项目所基于的移植',
    'Игра по сети, DLSS, страница читов, добавление в Steam, значок, пропуск конвейеров, которые драйвер не может создать, и игра без вылета при нехватке видеопамяти': '联机、DLSS、作弊页面、添加到 Steam、图标、跳过驱动无法创建的管线，以及显存耗尽时不再崩溃',
    'Собрал и адаптировал десятки исправлений: вылеты при загрузке, чёрные изображения, апскейлер, строка производительности в журнале': '收集并改编了数十项修复：加载时崩溃、黑色图像、超分辨率、日志中的性能行',
    'Чёрный предпросмотр персонажа, картинка экрана загрузки и память кэша текстур': '黑色的角色预览、加载画面图片与纹理缓存的内存',
    'Кэш текстур вовремя освобождает видеопамять': '纹理缓存及时释放显存',
    'Вылеты при загрузке областей': '加载区域时的崩溃',
    'Интерфейс, пропадавший не в 1080p, векторы движения больших чудовищ и ошибка памяти': '非 1080p 下消失的界面、大型野兽的运动矢量与一处内存错误',
    'Вылеты при загрузке некоторых карт и меню жестов с клавиатуры': '加载部分地图时的崩溃与键盘打开的手势菜单',
    'Экранная клавиатура для имени персонажа и уведомление о компиляции шейдеров': '角色名的屏幕键盘与着色器编译提示',
    'Сетевые библиотеки игры по сети и сервер для своего кооператива': '联机库与自建合作服务器',
    'Основа поддержки DLSS и модель FSR 4 без шлейфов за персонажами': 'DLSS 支持的基础，以及角色身后无拖影的 FSR 4 模型',
    'Апскейлер FSR 3.1': 'FSR 3.1 超分辨率',
    'Игра запускается, когда DLSS нельзя использовать': '无法使用 DLSS 时游戏仍可启动',
    'Перевод на упрощённый китайский': '简体中文翻译',
    'Звук игры на полной громкости': '游戏音频满音量',
    'Флажки и ползунки внутриигрового меню': '游戏内菜单的复选框与滑块',
    'Подробные отчёты с журналами и проверка исправлений': '附带日志的详细报告与修复测试',
    'Идея поменять местами A и B на контроллерах в стиле Nintendo': '在任天堂风格手柄上交换 A 与 B 的建议',
    'Проверка исправления видеопамяти': '测试显存修复',
    'Рендерер и компилятор шейдеров': '渲染器与着色器重编译器',
    'Инструмент для сборки AppImage': '构建 AppImage 的工具',
    'Нашёл ошибку, из-за которой игра не запускалась на некоторых видеокартах, и ускорение камеры на DualShock 4': '发现了导致游戏在部分显卡上无法启动的错误，以及 DualShock 4 上的镜头加速',
    'Нашёл, почему игра не запускалась в игровом режиме Steam Deck': '找出了游戏在 Steam Deck 游戏模式下无法启动的原因',
    'Нашёл, при каких эффектах зависают загрузки на NVIDIA': '找出了哪些效果会让 NVIDIA 上的加载画面卡住',
    'ps4-pkg-extractor: установка игры из файлов .pkg': 'ps4-pkg-extractor：从 .pkg 文件安装游戏',
    # Shader cache
    'Кэш шейдеров': '着色器缓存',
    'Очистить': '清除',
    '{}. Если после обновления картинка выглядит странно, очистите его: шейдеры соберутся заново (первые минуты в каждой зоне возможны рывки)': '{}。如果更新后画面异常，请清除：着色器会重新生成（每个区域的前几分钟可能卡顿）',
    'Пусто: шейдеры соберутся при игре': '空：着色器会在游玩时生成',
    'Очистить кэш шейдеров?': '清除着色器缓存？',
    'Игра соберёт шейдеры заново: первые минуты в каждой зоне возможны рывки. Сохранения и настройки не затрагиваются.': '游戏会重新生成着色器：每个区域的前几分钟可能卡顿。存档和设置不受影响。',
    'Названия трофеев на английском без ключа и звук при получении трофея': '无密钥时的英文奖杯名称与获得奖杯时的音效',
    'Буфер трафарета, в который писали цветные изображения': '被颜色图像写入的模板缓冲区',
    'Вход на публичный сервер shadNet без отключения': '在公共 shadNet 服务器上保持登录',
    'Установить из PKG': '从 PKG 安装',
    'Выбрать .pkg…': '选择 .pkg…',
    'Файлы .pkg: игра, обновление, DLC': '.pkg 文件：游戏、更新、DLC',
    'Куда установить игру': '游戏安装位置',
    'Установка…': '正在安装…',
    'Игра установлена: {}': '游戏已安装：{}',
    'Не удалось установить: подробности в журнале': '无法安装：详情见日志',
    'Выход из игры из меню с контроллера, меню в пределах экрана и половины тачпада на Xbox': '用手柄从菜单退出游戏、菜单不超出屏幕，以及 Xbox 手柄上的触摸板左右两半',
    'Вылет видеоплеера при его остановке': '视频播放器停止时的崩溃',
    'Язык внутриигрового меню при запуске без окна лаунчера': '不经启动器窗口启动时游戏内菜单的语言',
    'DLSS в AppImage на NVIDIA': 'NVIDIA 上 AppImage 中的 DLSS',
    'Сверхширокие мониторы без растянутой картинки': '超宽屏显示器画面不再被拉伸',
    'Движение с клавиатуры: круглая диагональ и последняя нажатая клавиша': '键盘移动：圆形斜向与最后按下的键',
    'Отладка вылетов: процесс ждёт отладчик (BB_FAULT_WAIT)': '崩溃调试：进程等待调试器（BB_FAULT_WAIT）',
    'Видеопамять на картах с 4 ГБ и вылеты: флипы, swapchain, дескрипторы и ошибки страниц; смена стиков и инверсия камеры, импорт сохранений, выбор версии': '4 GB 显卡的显存与崩溃：翻转、交换链、描述符和页错误；交换摇杆与视角反转、导入存档、版本选择',
    'Большие группы команд записи и swapchain после изменений экрана': '大型录制命令组以及显示变化后的交换链',
    # GODZILLA (gzport)
    'GODZILLA {}, версия 1.01':
        'GODZILLA {}，版本 1.01',
    'GODZILLA добавлена в библиотеку Steam':
        'GODZILLA 已添加到 Steam 库',
    'GODZILLA — товарный знак Toho Co., Ltd.; игра для PS4 издана Bandai Namco Entertainment. Этот проект с ними не связан.':
        'GODZILLA 是 Toho Co., Ltd. 的商标；PS4 游戏由 Bandai Namco Entertainment 发行。本项目与它们无关。',
    'XML-патчи в формате shadPS4 для версии 01.01 из папки патчей. Применяются при запуске.':
        '补丁文件夹中、shadPS4 格式、适用于 01.01 版本的 XML 补丁。会在游戏启动时生效。',
    'eboot.bin не от версии 1.01: скопируйте eboot.bin из дампа обновления 1.01 в папку игры с заменой':
        'eboot.bin 不是 1.01 版本：请将 1.01 更新转储中的 eboot.bin 复制到游戏文件夹并覆盖',
    'gzport — нативный порт для Linux':
        'gzport — 原生 Linux 移植版',
    'Авторы bbport и bloodborne_linux, на которых построен gzport, и все, кто им помогал':
        'gzport 所基于的 bbport 和 bloodborne_linux 的作者，以及所有帮助过他们的人',
    'В папке игры нет: {}. Распакуйте игру и обновление 1.01 заново':
        '游戏文件夹中缺少：{}。请重新解包游戏和 1.01 更新',
    'В этой папке нет сохранений GODZILLA (SAVEDATA00 с DATA.BIN)':
        '此文件夹中没有 GODZILLA 存档（含 DATA.BIN 的 SAVEDATA00）',
    'Игра идёт с 60 FPS, как на PS4. Выше 60 FPS: нужен патч частоты кадров, его пока нет':
        '游戏以 60 FPS 运行，与 PS4 一致。高于 60 FPS 需要帧率补丁，目前尚无',
    'Для GODZILLA пока недоступен: игра рисует кадр прямо в разрешении вывода':
        'GODZILLA 暂不可用：游戏直接以输出分辨率绘制画面',
    'Игра, обновление 1.01 и DLC из ваших файлов .pkg':
        '从你的 .pkg 文件安装游戏、1.01 更新和 DLC',
    'Ключ трофеев PS4 (TrophyKey в shadPS4), 32 шестнадцатеричных символа: с ним названия и описания на языке игры. Хранится на этом компьютере. Без него видны только значки':
        'PS4 的奖杯密钥（shadPS4 中的 TrophyKey），32 位十六进制数：填写后奖杯名称和说明使用游戏语言。仅保存在本机。未填写时只显示图标',
    'Нативный порт для Linux, версия {}':
        '原生 Linux 移植版，版本 {}',
    'Нужен патч для версии 1.01, его пока нет':
        '需要适用于 1.01 版本的补丁，目前尚无',
    'Нужно обновление 1.01: скопируйте файлы дампа обновления 1.01 в папку игры с заменой (найдена версия {})':
        '需要 1.01 更新：请将转储出的 1.01 更新文件复制到游戏文件夹并覆盖（当前检测到版本 {}）',
    'Основано на bloodborne_linux от ayozetr':
        '基于 ayozetr 的 bloodborne_linux',
    'bloodborne_linux: порт для Linux, на котором построен gzport':
        'bloodborne_linux：gzport 所基于的 Linux 移植版',
    'Папка с сохранениями GODZILLA':
        'GODZILLA 存档文件夹',
    'Патчи игры':
        '游戏补丁',
    'Португальский (Бразилия)':
        '葡萄牙语（巴西）',
    'Это не GODZILLA (найдено {}): нужна GODZILLA (CUSA02046) с обновлением 1.01':
        '这不是 GODZILLA（检测到 {}）：需要带 1.01 更新的 GODZILLA（CUSA02046）',
    'Тачпад, левая половина':
        '触摸板左侧',
    'Тачпад, правая половина':
        '触摸板右侧',
    'Настройки по умолчанию':
        '默认设置',
    'Восстановить мои настройки по умолчанию':
        '恢复我的默认设置',
    'Вернуть':
        '恢复',
    'Сохранить текущие как мои настройки по умолчанию':
        '将当前设置保存为我的默认设置',
    'Настройки лаунчера и bbport.ini, без назначений кнопок':
        '启动器和 bbport.ini 的设置，不含按键映射',
    'Сохранить':
        '保存',
    'Из {}':
        '来自 {}',
    'Своих настроек по умолчанию пока нет: восстанавливаются встроенные (папки и ключ трофеев не меняются)':
        '尚无自己的默认设置：将恢复内置默认值（文件夹和奖杯密钥保持不变）',
    'Не удалось прочитать {}':
        '无法读取 {}',
    'Восстановить настройки по умолчанию?':
        '恢复默认设置？',
    'Настройки лаунчера и bbport.ini станут такими, как в {}. Остальные строки bbport.ini, в том числе назначения кнопок, не меняются':
        '启动器和 bbport.ini 的设置将变为 {} 中的设置。bbport.ini 的其他行（包括按键映射）保持不变',
    'Своих настроек по умолчанию нет: настройки лаунчера и bbport.ini станут встроенными. Папки, ключ трофеев и назначения кнопок не меняются':
        '没有自己的默认设置：启动器和 bbport.ini 的设置将恢复为内置默认值。文件夹、奖杯密钥和按键映射保持不变',
    'Настройки по умолчанию восстановлены':
        '已恢复默认设置',
    'Сохранить текущие настройки как свои по умолчанию?':
        '将当前设置保存为您的默认设置？',
    'Они запишутся в {} вместо прежних, и «Вернуть» будет восстанавливать их':
        '它们将写入 {} 并替换之前的设置，“恢复”会回到这些设置',
    'Не удалось сохранить {}':
        '无法保存 {}',
    'Текущие настройки сохранены как ваши по умолчанию':
        '当前设置已保存为您的默认设置',
    # Online page (LAN versus)
    "Версус по локальной сети: VS MODE в меню «Онлайн» игры, через ваш сервер shadNet (shadnet-p2p с патчем gzport). У каждого игрока своя учётная запись на этом сервере": "局域网对战：游戏「Online」菜单中的 VS MODE，通过你自己的 shadNet 服务器（带 gzport 补丁的 shadnet-p2p）。每位玩家在该服务器上都有自己的账户",
    "Как настроить версус по сети": "如何设置联网对战",
    "Имя учётной записи на сервере shadNet (оно же ваше имя в игре) и её пароль. Пароль хранится на этом компьютере вместе с настройками лаунчера": "你在 shadNet 服务器上的账户名（也是你在游戏中的名字）及其密码。密码与启动器设置一起保存在这台电脑上",
    "Порт P2P (UDP)": "P2P 端口（UDP）",
    "Через него игроки соединяются напрямую; он должен быть открыт между компьютерами": "玩家通过它直接相连；它必须在各电脑之间开放",
    "Укажите адрес сервера": "请输入服务器地址",
    "UDP сервера shadNet": "shadNet 服务器 UDP",
    "отвечает; сервер видит этот компьютер как {}": "有响应；服务器看到这台电脑为 {}",
    "не отвечает: матч не соединится": "无响应：对战将无法连接",
}

# Translations by language code; Russian is the key itself. Strings missing in a translation
# fall back to English, not to the Russian key.
TRANSLATIONS = {"en": EN, "pt_BR": PT_BR, "es": ES, "it": IT, "fr": FR, "de": DE,
                "zh_CN": ZH_CN}
LANGUAGES = ("ru", *TRANSLATIONS)


def system_locale(env=os.environ):
    """The desktop's locale, lower case with underscores ("es_es.utf_8"), or ""."""
    for key in ("LC_ALL", "LC_MESSAGES", "LANG", "LANGUAGE"):
        value = env.get(key, "")
        if value:
            return value.lower().replace("-", "_")
    return ""


def system_language():
    locale = system_locale()
    if locale.startswith("pt_br"):
        return "pt_BR"
    if locale.startswith("zh"):
        return "zh_CN"
    short = locale[:2]
    return short if short in LANGUAGES else "en"


# The PS4 system language (sceSystemServiceParamGetInt) the game picks its text and voices by,
# for the languages the game has; anything else gets English.
GAME_LANGUAGES = {"ja": 0, "en": 1, "fr": 2, "es": 3, "de": 4, "it": 5, "ru": 8}


def system_game_language(env=os.environ):
    return GAME_LANGUAGES.get(system_locale(env)[:2], 1)


_language = "ru"


def set_language(choice):
    """choice: one of LANGUAGES or "" (the system's)."""
    global _language
    _language = choice if choice in LANGUAGES else system_language()


def language():
    return _language


def tr(text):
    table = TRANSLATIONS.get(_language)
    if table is None:
        return text
    return table.get(text, EN.get(text, text))

