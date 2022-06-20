#
# SMIRK
# Copyright (C) 2021-2022 RISE Research Institutes of Sweden AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import argparse

from tests.system.system_test_runner import (
    PedestrianTestConfiguration,
    SystemTestRunner,
)

pedestrian_all_pairs = [
    PedestrianTestConfiguration(
        pedestrian_appearance="child",
        pedestrian_start_x=21.5,
        pedestrian_start_y=5,
        pedestrian_angle=-45,
        pedestrian_speed=1,
        car_speed=3.47,
        scenario_id="TC-1",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="child",
        pedestrian_start_x=26,
        pedestrian_start_y=5,
        pedestrian_angle=-90,
        pedestrian_speed=1,
        car_speed=5.78,
        scenario_id="TC-2",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="child",
        pedestrian_start_x=38,
        pedestrian_start_y=0,
        pedestrian_angle=0,
        pedestrian_speed=0,
        car_speed=14,
        scenario_id="TC-3",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="child",
        pedestrian_start_x=54.5,
        pedestrian_start_y=-5,
        pedestrian_angle=135,
        pedestrian_speed=3,
        car_speed=18.9,
        scenario_id="TC-4",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_business",
        pedestrian_start_x=20,
        pedestrian_start_y=0,
        pedestrian_angle=180,
        pedestrian_speed=3,
        car_speed=16,
        scenario_id="TC-5",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_business",
        pedestrian_start_x=23.5,
        pedestrian_start_y=5,
        pedestrian_angle=-45,
        pedestrian_speed=1,
        car_speed=3.73,
        scenario_id="TC-6",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_business",
        pedestrian_start_x=46,
        pedestrian_start_y=5,
        pedestrian_angle=-135,
        pedestrian_speed=1,
        car_speed=5.8,
        scenario_id="TC-7",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_business",
        pedestrian_start_x=50,
        pedestrian_start_y=-5,
        pedestrian_angle=90,
        pedestrian_speed=1,
        car_speed=10,
        scenario_id="TC-8",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_casual",
        pedestrian_start_x=15,
        pedestrian_start_y=0,
        pedestrian_angle=135,
        pedestrian_speed=0,
        car_speed=11,
        scenario_id="TC-9",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_casual",
        pedestrian_start_x=24.5,
        pedestrian_start_y=-5,
        pedestrian_angle=135,
        pedestrian_speed=1,
        car_speed=3.14,
        scenario_id="TC-10",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_casual",
        pedestrian_start_x=45,
        pedestrian_start_y=5,
        pedestrian_angle=-135,
        pedestrian_speed=1,
        car_speed=5.66,
        scenario_id="TC-11",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_casual",
        pedestrian_start_x=46,
        pedestrian_start_y=5,
        pedestrian_angle=-90,
        pedestrian_speed=1,
        car_speed=10.22,
        scenario_id="TC-12",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="female_casual",
        pedestrian_start_x=50.5,
        pedestrian_start_y=6,
        pedestrian_angle=-45,
        pedestrian_speed=3,
        car_speed=18.6,
        scenario_id="TC-13",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_business",
        pedestrian_start_x=21,
        pedestrian_start_y=-5,
        pedestrian_angle=45,
        pedestrian_speed=1,
        car_speed=3.68,
        scenario_id="TC-14",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_business",
        pedestrian_start_x=25,
        pedestrian_start_y=5,
        pedestrian_angle=-90,
        pedestrian_speed=3,
        car_speed=15,
        scenario_id="TC-15",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_business",
        pedestrian_start_x=26.5,
        pedestrian_start_y=5,
        pedestrian_angle=-135,
        pedestrian_speed=1,
        car_speed=3.46,
        scenario_id="TC-16",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_business",
        pedestrian_start_x=54,
        pedestrian_start_y=0,
        pedestrian_angle=0,
        pedestrian_speed=1,
        car_speed=9,
        scenario_id="TC-17",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_casual",
        pedestrian_start_x=34,
        pedestrian_start_y=-5,
        pedestrian_angle=45,
        pedestrian_speed=1,
        car_speed=5.52,
        scenario_id="TC-18",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_casual",
        pedestrian_start_x=34.5,
        pedestrian_start_y=5,
        pedestrian_angle=-135,
        pedestrian_speed=1,
        car_speed=4.71,
        scenario_id="TC-19",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_casual",
        pedestrian_start_x=47.5,
        pedestrian_start_y=4,
        pedestrian_angle=-45,
        pedestrian_speed=1,
        car_speed=10.3,
        scenario_id="TC-20",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_casual",
        pedestrian_start_x=74,
        pedestrian_start_y=0,
        pedestrian_angle=90,
        pedestrian_speed=0,
        car_speed=19,
        scenario_id="TC-21",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_construction",
        pedestrian_start_x=10,
        pedestrian_start_y=5,
        pedestrian_angle=-90,
        pedestrian_speed=3,
        car_speed=6,
        scenario_id="TC-22",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_construction",
        pedestrian_start_x=17.5,
        pedestrian_start_y=-5,
        pedestrian_angle=45,
        pedestrian_speed=1,
        car_speed=3.46,
        scenario_id="TC-23",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_construction",
        pedestrian_start_x=39,
        pedestrian_start_y=5,
        pedestrian_angle=-135,
        pedestrian_speed=1,
        car_speed=4.81,
        scenario_id="TC-24",
    ),
    PedestrianTestConfiguration(
        pedestrian_appearance="male_construction",
        pedestrian_start_x=86.5,
        pedestrian_start_y=5,
        pedestrian_angle=-135,
        pedestrian_speed=1,
        car_speed=12.89,
        scenario_id="TC-25",
    ),
]


def test_pedestrian_all_pairs(add_noise: bool = False):
    runner = SystemTestRunner()
    runner.run_all(pedestrian_all_pairs, add_noise)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--noisy",
        help="Randomly add jitter in the range from -10%% to +10%% to all numerical values.",
        action="store_true",
    )
    args = parser.parse_args()

    test_pedestrian_all_pairs(args.noisy)
