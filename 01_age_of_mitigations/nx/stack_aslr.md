### Disable stack aslr (system wide)
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

### Enable stack aslr (default on most modern Linux systems)
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
