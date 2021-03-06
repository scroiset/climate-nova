# Copyright (c) 2013 Julien Danjou <julien@danjou.info>
# Copyright (c) 2013 Swann Croiset <swann.croiset@bull.net>
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo.config import cfg
#NOTE(scroiset): resolve conflict with nova
cfg.CONF.unregister_opt(cfg.StrOpt('default_log_levels'))

from climate.openstack.common import log as logging
from nova.scheduler import filters

LOG = logging.getLogger(__name__)


class ClimateFilter(filters.BaseHostFilter):
    """Climate Filter for nova-scheduler."""

    run_filter_once_per_request = True

    def host_passes(self, host_state, filter_properties):
        """Filter based on Climate."""
        # scheduler_hints = filter_properties.get('scheduler_hints') or {}
        # XXX send host_state + to Climate API
        return True
