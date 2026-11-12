#!/usr/bin/env bash
# Creates one "XYZ function required" issue per skeletal function and
# assigns it to its prime. Safe to re-run: existing issues are not
# duplicated, only (re)assigned. Fill in the teammates' GitHub usernames
# below and re-run to assign their issues.
set -euo pipefail

SAMITH_GH="samith01"
RYAN_GH="samith01"     # all assigned to samith01 for now
KLARA_GH="samith01"

# function|file|owner
FUNCS="
setup()|main.py|samith
update(state)|main.py|samith
main()|main.py|samith
init_knobs(x_pin, y_pin)|knob_reader.py|klara
read_raw(adc)|knob_reader.py|klara
smooth_reading(history, new_value, size)|knob_reader.py|klara
map_range(value, in_min, in_max, out_min, out_max)|knob_reader.py|klara
read_target_xy(x_adc, y_adc, x_hist, y_hist)|knob_reader.py|klara
init_button(pin)|pen_button.py|klara
is_pressed(button)|pen_button.py|klara
debounce_press(button, last_state, last_time_ms, now_ms)|pen_button.py|klara
toggle_pen(pen_down)|pen_button.py|klara
distance_to_shoulder(x, y)|arm_angles.py|ryan
clamp_to_reach(x, y)|arm_angles.py|ryan
elbow_angle(d)|arm_angles.py|ryan
shoulder_angle(x, y, d)|arm_angles.py|ryan
angles_within_limits(shoulder, elbow)|arm_angles.py|ryan
xy_to_angles(x, y)|arm_angles.py|ryan
init_servos(pins, freq)|servo_driver.py|samith
angle_to_duty(angle, cal)|servo_driver.py|samith
set_servo_angle(pwm, angle, cal)|servo_driver.py|samith
move_arm(servos, shoulder, elbow)|servo_driver.py|samith
set_pen(servos, pen_down)|servo_driver.py|samith
park_arm(servos)|servo_driver.py|samith
"

declare -A NAME=([samith]="Samith Fernando" [ryan]="Ryan Hannum Horne" [klara]="Klara Kerekes")
declare -A GH=([samith]="$SAMITH_GH" [ryan]="$RYAN_GH" [klara]="$KLARA_GH")

# Labels: one per module
for f in main knob_reader pen_button arm_angles servo_driver; do
  gh label create "module:$f" --color 1D76DB --force >/dev/null
done

existing=$(gh issue list --state all --limit 200 --json number,title \
  --jq '.[] | "\(.number)\t\(.title)"')

echo "$FUNCS" | while IFS='|' read -r sig file owner; do
  [ -z "$sig" ] && continue
  name="${sig%%(*}"
  title="$name function required"
  assignee="${GH[$owner]}"
  num=$(printf '%s\n' "$existing" | awk -F'\t' -v t="$title" '$2==t {print $1; exit}')

  if [ -n "$num" ]; then
    if [ -n "$assignee" ]; then
      gh issue edit "$num" --add-assignee "$assignee" >/dev/null
      echo "#$num $title -> assigned $assignee"
    else
      echo "#$num $title (exists, no username yet)"
    fi
    continue
  fi

  body="Function: \`$sig\` in \`$file\`
Prime: ${NAME[$owner]}

See the header (docstring) in \`$file\` for inputs, outputs and operation.

Done when:
- [ ] Function implemented
- [ ] Unit tests written and passing
- [ ] Code and tests merged into main together"

  args=(--title "$title" --body "$body" --label "module:${file%.py}")
  [ -n "$assignee" ] && args+=(--assignee "$assignee")
  gh issue create "${args[@]}"
done
