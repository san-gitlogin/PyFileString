from fileOperations import fileOperations
import configparser
import os
import shutil
from datetime import datetime


fileObject = fileOperations()

def backup_file(file_path):
    """
    This keyword makes a backup of the input file in the current execution directory. It returns success
    or exception based on the event.

    Example usage:
        | backup_file | file_path = <String><Path>
    """
    current_date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    source_path = file_path
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, f"Backup_{current_date_time}")
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    destination_path = os.path.join(os.getcwd(), f"{final_directory}\\Backup_file_{current_date_time}")

    try:
        if os.path.isfile(source_path):
            shutil.copyfile(source_path, destination_path)
        return f"Backup Success at {destination_path}"
    except Exception as e:
        return e
    

#Reading the configs and performing the functions
def read_config(config_path, file_path):
    """
    This keyword reads the config file for input data and calls the respective functions based on the 
    sections in the config file. The output is returned in the form of dict containing fsif outputs.

    Example usage:
        | read_config | config_path = <String><Path> | file_path = <String><Path>
    """
    config = configparser.ConfigParser()
    with open(config_path) as file_handle:
        config.read_file(file_handle)

    sections = config.sections()

    for section in sections:
        match section:
            case "FSIF and number of occurrences":
                try:
                    search_string = config.get(section,'search_string')
                    case_sensitive = config.getboolean(section, 'case_sensitive')
                    return fileObject.fsif_and_number_of_occurences(filePath = file_path, searchString = search_string, caseSensitive = case_sensitive)
                except Exception as e:
                    return e
            case "FSIF and print first n occurrences":
                try:
                    n = config.getint(section, 'n')
                    search_string = config.get(section,'search_string')
                    case_sensitive = config.getboolean(section, 'case_sensitive')
                    return fileObject.fsif_and_first_n_occurences(filePath = file_path, searchString = search_string, caseSensitive = case_sensitive, n=n)
                except Exception as e:
                    return e

            case "FSIF and print last n occurrences":
                try:
                    n = config.getint(section, 'n')
                    search_string = config.get(section,'search_string')
                    case_sensitive = config.getboolean(section, 'case_sensitive')
                    return fileObject.fsif_and_last_n_occurences(filePath = file_path, searchString = search_string, caseSensitive = case_sensitive, n=n)
                except Exception as e:
                    return e

            case "FSIF and replace all occurrences":
                backup_status = backup_file(file_path)
                if "Backup Success" in backup_status:
                    try:
                        search_string = config.get(section,'search_string')
                        replace_string = config.get(section, 'replace_string')
                        case_sensitive = config.getboolean(section, 'case_sensitive')
                        return fileObject.fsif_and_replace_all_occurences(filePath = file_path, searchString = search_string, replaceString = replace_string, caseSensitive = case_sensitive)
                    except Exception as e:
                        return e

            case "FSIF and replace nth occurrence at a line number":
                backup_status = backup_file(file_path)
                if "Backup Success" in backup_status:
                    try:
                        search_string = config.get(section,'search_string')
                        replace_string = config.get(section, 'replace_string')
                        occurence_number = config.getint(section, 'occurence_number')
                        line_number = config.getint(section, 'line_number')
                        case_sensitive = config.getboolean(section, 'case_sensitive')
                        return fileObject.fsif_and_replace_occurence_at_line(filePath = file_path, searchString = search_string, replaceString = replace_string, occurenceNumber = occurence_number, lineNumber = line_number, caseSensitive = case_sensitive)
                    except Exception as e:
                        return e

            case "FSIF and its nth occurrence including all occurence and print the line number and contents":
                try:
                    search_string = config.get(section,'search_string')
                    occurence_number = config.getint(section, 'occurence_number')
                    case_sensitive = config.getboolean(section, 'case_sensitive')
                    return fileObject.fsif_and_number_of_occurences_and_nth_line(filePath = file_path, searchString = search_string, occurenceNumber = occurence_number, caseSensitive = case_sensitive)
                except Exception as e:
                    return e

            case "FSIF and print and store x lines above and y lines below":
                try:
                    search_string = config.get(section,'search_string')
                    x_lines_count = config.getint(section, 'x_lines_count')
                    y_lines_count = config.getint(section, 'y_lines_count')
                    case_sensitive = config.getboolean(section, 'case_sensitive')
                    return fileObject.fsif_and_print_store_xy_lines(filePath = file_path, searchString = search_string, xLinesCount = x_lines_count, yLinesCount = y_lines_count, caseSensitive = case_sensitive)
                except Exception as e:
                    return e

            case "FSIF and replace only if n lines above matches":
                backup_status = backup_file(file_path)
                if "Backup Success" in backup_status:
                    try:
                        search_string = config.get(section,'search_string')
                        replace_string = config.get(section, 'replace_string')
                        above_line_content = config.get(section, 'above_line_content')
                        case_sensitive = config.getboolean(section, 'case_sensitive')
                        return fileObject.fsif_and_replace_above_line_match(filePath = file_path, searchString = search_string, replaceString = replace_string, aboveLineContent = above_line_content, caseSensitive = case_sensitive)
                    except Exception as e:
                        return e

            case "FSIF and replace only if n lines below matches":
                backup_status = backup_file(file_path)
                if "Backup Success" in backup_status:
                    try:
                        search_string = config.get(section,'search_string')
                        replace_string = config.get(section, 'replace_string')
                        below_line_content = config.get(section, 'below_line_content')
                        case_sensitive = config.getboolean(section, 'case_sensitive')
                        return fileObject.fsif_and_replace_below_line_match(filePath = file_path, searchString = search_string, replaceString = replace_string, belowLineContent = below_line_content, caseSensitive = case_sensitive)
                    except Exception as e:
                        return e

            case "FSIF and replace only if n lines above and m lines below matches":
                backup_status = backup_file(file_path)
                if "Backup Success" in backup_status:
                    try:
                        search_string = config.get(section,'search_string')
                        replace_string = config.get(section, 'replace_string')
                        above_line_content = config.get(section, 'above_line_content')
                        below_line_content = config.get(section, 'below_line_content')
                        case_sensitive = config.getboolean(section, 'case_sensitive')
                        return fileObject.fsif_and_replace_n_and_m_line_match(filePath = file_path, searchString = search_string, replaceString = replace_string, aboveLineContent = above_line_content, belowLineContent = below_line_content, caseSensitive = case_sensitive)
                    except Exception as e:
                        return e

            case "FSIF and replace nth line with another string before the match":
                backup_status = backup_file(file_path)
                if "Backup Success" in backup_status:
                    try:
                        line_number = config.getint(section, 'line_number')
                        search_string = config.get(section,'search_string')
                        replace_string = config.get(section, 'replace_string')
                        below_line_content = config.get(section, 'below_line_content')
                        case_sensitive = config.getboolean(section, 'case_sensitive')
                        return fileObject.fsif_and_replace_nth_below_line_match(filePath = file_path, lineNumber = line_number, searchString = search_string, replaceString = replace_string, belowLineContent = below_line_content, caseSensitive = case_sensitive)
                    except Exception as e:
                        return e

            case "FSIF and replace nth line with another string after the match":
                backup_status = backup_file(file_path)
                if "Backup Success" in backup_status:
                    try:
                        line_number = config.getint(section, 'line_number')
                        search_string = config.get(section,'search_string')
                        replace_string = config.get(section, 'replace_string')
                        above_line_content = config.get(section, 'above_line_content')
                        case_sensitive = config.getboolean(section, 'case_sensitive')
                        return fileObject.fsif_and_replace_nth_above_line_match(filePath = file_path, lineNumber = line_number, searchString = search_string, replaceString = replace_string, aboveLineContent = above_line_content, caseSensitive = case_sensitive)
                    except Exception as e:
                        return e
            
            case _:
                return f"{section} related operations not found"
            