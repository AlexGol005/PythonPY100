average_time_for_1_task_min = int(input('Введите среднее время выполнения 1 задания, минут: '))
average_time_for_1_task_hour = average_time_for_1_task_min / 60
time_need_for_10_tasks = round(10 * average_time_for_1_task_hour, 2)
print('на выполнение 10 заданий вы потратите ', time_need_for_10_tasks, 'часов')
