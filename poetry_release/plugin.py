from poetry.plugins.application_plugin import ApplicationPlugin    # type: ignore

from poetry_release.command import release_factory


class ReleasePlugin(ApplicationPlugin):         # type: ignore
    def activate(self, application) -> None:    # type: ignore
        application.command_loader.register_factory("release", release_factory)

