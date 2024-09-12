import random
def read_coromon_data(file_path):
    coromon_data = {}
    with open(file_path, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            coromon_name = values[0]
            coromon_type = values[1]
            coromon_data[coromon_name] = {}
            for index in range(2, len(header)):
                coromon_properties = coromon_data[coromon_name]
                property_name = header[index]
                property_value = values[index]
                coromon_properties[property_name] = property_value
                coromon_properties['Type'] = coromon_type
    return coromon_data
def info(coromon_data):
    total_coromons = len(coromon_data)
    print("Total coromons:", total_coromons)
    random_coromon_name = random.choice(list(coromon_data.keys()))
    random_coromon = coromon_data[random_coromon_name]
    print("Random Coromon:", random_coromon_name, "-", random_coromon)
    coromon_types = []
    for coromon in coromon_data.values():
        if coromon['Type'] not in coromon_types:
            coromon_types.append(coromon['Type'])
    print("Coromon Types:", ", ".join(coromon_types))
    for property_name in random_coromon.keys():
        if property_name != 'Coromon' and property_name != 'Type':
            print("Average", property_name, "for each Coromon type:")
            averages = []
            for coromon_info in coromon_data.items():
                coromon_name = coromon_info[0]
                coromon = coromon_info[1]
                if coromon[property_name].isdigit():  
                    value = int(coromon[property_name])
                    averages.append((coromon['Type'], value))
            type_averages = {}
            type_counts = {}
            for entry in averages:
                coromon_type = entry[0]
                value = entry[1]
                type_averages[coromon_type] = type_averages.get(coromon_type, 0) + value
                type_counts[coromon_type] = type_counts.get(coromon_type, 0) + 1
            def calculate_average_ratio(coromon_type):
                if type_counts[coromon_type] > 0:
                    denominator = type_counts[coromon_type]
                return type_averages[coromon_type] / denominator

            for coromon_type in coromon_types:
                if type_counts[coromon_type] > 0:
                    denominator = type_counts[coromon_type]
                    average_value = type_averages.get(coromon_type, 0) / denominator
                    print(coromon_type, ":", average_value)
            first_coromon_type = None
            for coromon_type in type_averages:
                first_coromon_type = coromon_type
                break
            highest_average_type = first_coromon_type
            lowest_average_type = first_coromon_type
            highest_average_value = calculate_average_ratio(first_coromon_type)
            lowest_average_value = calculate_average_ratio(first_coromon_type)
            for coromon_type in type_averages:
                average_value = calculate_average_ratio(coromon_type)
            if average_value > highest_average_value:
                highest_average_value = average_value
                highest_average_type = coromon_type
            if average_value < lowest_average_value:
                lowest_average_value = average_value
                lowest_average_type = coromon_type
            print(property_name,"- Type with the Highest average:",highest_average_type)
            print(property_name,"- Type with the Highest average:",lowest_average_type)
coromon_data = read_coromon_data('CoromonDataset.csv')
info(coromon_data)