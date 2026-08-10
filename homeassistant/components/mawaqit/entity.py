"""Base entity for the Mawaqit integration."""

from typing import override

from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, MAWAQIT_URL
from .coordinator import PrayerTimeCoordinator


class MawaqitEntity(CoordinatorEntity[PrayerTimeCoordinator]):
    """Defines a base Mawaqit entity, tied to the configured mosque."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: PrayerTimeCoordinator,
        mosque_uuid: str,
        mosque_name: str | None,
    ) -> None:
        """Initialize the Mawaqit entity."""
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, mosque_uuid)},
            name=mosque_name,
            manufacturer="MAWAQIT",
            entry_type=DeviceEntryType.SERVICE,
            configuration_url=MAWAQIT_URL,
        )

    @property
    @override
    def available(self) -> bool:
        """Return True if entity is available."""
        return super().available and self.coordinator.data is not None
