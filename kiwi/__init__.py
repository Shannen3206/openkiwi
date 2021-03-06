#  OpenKiwi: Open-Source Machine Translation Quality Estimation
#  Copyright (C) 2019 Unbabel <openkiwi@unbabel.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from kiwi.lib.train import train_from_file as train  # NOQA
from kiwi.lib.predict import load_model  # NOQA

from kiwi.lib.predict import predict_from_file as predict
from kiwi.lib.evaluate import evaluate_from_file as evaluate

__version__ = '0.1.2'
__copyright__ = (
    '2019 Unbabel. All rights reserved. '
    'Source code available under the AGPL-3.0.'
)
