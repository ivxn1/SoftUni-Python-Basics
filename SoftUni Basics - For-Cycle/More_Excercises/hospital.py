period_days = int(input())
doctors = 7
patients_not_checked = 0
patients_checked = 0

for day in range(1, period_days + 1):
    if day % 3 == 0:
        if patients_not_checked > patients_checked:
            doctors += 1
    patients_for_the_day = int(input())
    if patients_for_the_day > doctors:
        patients_not_checked += patients_for_the_day - doctors
        patients_checked += doctors
    else: patients_checked += patients_for_the_day

print(f'Treated patients: {patients_checked}.')
print(f'Untreated patients: {patients_not_checked}.')
