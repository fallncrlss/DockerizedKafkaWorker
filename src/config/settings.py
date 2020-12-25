from dynaconf import Dynaconf


settings: Dynaconf = Dynaconf(settings_files=['src/config/settings.toml'])
