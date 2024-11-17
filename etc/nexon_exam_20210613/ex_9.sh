for index in "${!my_array[@]}"; do
  (( index % 2 == 0)) && echo "${my_array[index]}"
done