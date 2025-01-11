# Exploring QNX System
### 1. Processes

A **process** in QNX is a running instance of a program, similar to processes in other operating systems. However, QNX's microkernel architecture makes its process model unique compared to traditional monolithic kernels like those in Linux.

#### 1.1. **Characteristics of QNX Processes**

- **Microkernel Architecture**:

  - The core functionality (e.g., memory management, process management, path resolution) is minimal and resides in the **microkernel**.

  - Most system-level functionality (e.g., file systems, networking, drivers) is implemented as **stand-alone processes** in user space. This design isolates services, improving fault tolerance.

- **Process Structure**:

  - Each process consists of:
    - **Threads**: Streams of execution within the process. Threads share the process's resources (e.g., memory, file descriptors).
    - **Address Space**: Virtual memory space unique to the process.

  - Processes communicate with each other via **Inter-Process Communication (IPC)**, managed by the **microkernel**.

- **First Process: `procnto-smp-instr`**:

  - The **first process** created when the system starts.

  - Hosts the Neutrino microkernel and provides basic system services:
    - **Process Manager**: Handles process creation and management.
    - **Memory Manager**: Manages virtual memory.
    - **Path Manager**: Resolves pathnames and links them to the appropriate servers or resources.

  - This process is critical for the system's operation.

- **Types of Processes**: QNX systems typically consist of three types of processes:

  - **Kernel Processes**: Provide core system functionality (e.g., procnto-smp-instr).

  - **System Services**: User-space processes that implement functionality typically found in a monolithic kernel:
    - File systems
    - Networking (TCP/IP stack)
    - USB
    - Graphics drivers
    - Audio

  - **Application Processes**: Implement specific user-facing or system-specific functionality:
    - Shell, editors, compilers and utilities. 
    - Media players, browsers (for interactive systems)
    - Controllers, monitors (for embedded systems in automotive, industrial, or medical use cases)

- **Customization**:

  - A QNX system can be customized to include only the processes necessary for its intended function:

    - A **headless system** (no display or GUI) may exclude graphics processes.

    - A **simple controller** may omit a permanent file system.

      >In some embedded systems, such as those used in industrial control, automotive, or simple IoT devices, the system may not require the traditional **file system** (like the ones you see on your computer: NTFS, ext4, FAT32)



#### 1.2.  **Process Management**

- **Process Creation**:

  - Processes are created by the **process manager** in the kernel.

  - Applications or system services can spawn new processes as needed.

- **Listing Processes and Threads**:

  - The `pidin` command lists all processes and their threads in a running QNX system.

  - Each process is identified by a unique **process ID (PID)**.

  ```bash
  pidin
  ```

  ```bash
  	  # The Output (truncated output)
        
        pid tid name                         prio STATE          Blocked                     
         1   1 /proc/boot/procnto-smp-instr   0f RUNNING                                    
         1   2 /proc/boot/procnto-smp-instr   0f RUNNING                                    
         1   3 /proc/boot/procnto-smp-instr   0f READY                                      
         1   4 /proc/boot/procnto-smp-instr   0f READY                                                                   
         1  11 /proc/boot/procnto-smp-instr 254i INTR                                       
         1  12 /proc/boot/procnto-smp-instr 254i INTR                                       
         1  13 /proc/boot/procnto-smp-instr   1f NANOSLEEP                                  
         1  15 /proc/boot/procnto-smp-instr  10r RECEIVE        1                               
         1  21 /proc/boot/procnto-smp-instr  10r RECEIVE        1                           
         1  22 /proc/boot/procnto-smp-instr  10r RECEIVE        1                           
         1  23 /proc/boot/procnto-smp-instr  10r RECEIVE        1                           
         1  24 /proc/boot/procnto-smp-instr  10r RECEIVE        1                           
         1  26 /proc/boot/procnto-smp-instr  10r RECEIVE        1                           
         1  27 /proc/boot/procnto-smp-instr  10r RUNNING                                    
     12291   1 proc/boot/slogger2            10r RECEIVE        1                           
     24580   1 proc/boot/devc-serminiuart    10r RECEIVE        1                           
     24580   2 proc/boot/devc-serminiuart   254i INTR                                       
     32774   1 proc/boot/ksh                 10r REPLY          24580                       
     36869   1 proc/boot/pci-server          10r RECEIVE        1                           
     36869   2 proc/boot/pci-server          10r RECEIVE        1                           
     36869   3 proc/boot/pci-server          10r RECEIVE        1                           
     36869   4 proc/boot/pci-server          10r RECEIVE        1                           
     57351   1 proc/boot/fsevmgr             10r SIGWAITINFO                                
     57351   2 proc/boot/fsevmgr             10r RECEIVE        1                           
     57351   3 proc/boot/fsevmgr             10r RECEIVE        2                              
    241677  20 system/bin/io-sock            10r CONDVAR        (0x0)                       
    241677  21 system/bin/io-sock            10r CONDVAR        (0x0)                       
    241677  22 system/bin/io-sock            10r CONDVAR        (0x0)                       
    241677  23 system/bin/io-sock            10r CONDVAR        (0x0)                       
    241677  24 system/bin/io-sock            10r CONDVAR        (0x0)                       
    241677  25 system/bin/io-sock            21r SEM            0                           
    241677  26 system/bin/io-sock            10r CONDVAR        (0x0)                       
    241677  27 system/bin/io-sock            10r CONDVAR        (0x0)                       
    241677  28 system/bin/io-sock            21r RECEIVE        6                           
    241677  29 system/bin/io-sock            21r RECEIVE        7                           
    241677  30 system/bin/io-sock            10r RECEIVE        8                           
    241677  31 system/bin/io-sock            10r RECEIVE        1                           
    241677  32 system/bin/io-sock            10r RECEIVE        1                           
    241677  33 system/bin/io-sock            10r RECEIVE        1                       
  ```

  >**Understanding the Columns** 
  >
  >1. **`pid` (Process ID):**
  >   - The unique identifier for each process running on the system.
  >   - For example, `1` is the `pid` of the `/proc/boot/procnto-smp-instr` process.
  >2. **`tid` (Thread ID):**
  >   - The unique identifier for each thread within a process.
  >   - A process can have multiple threads, and each thread has a `tid`.
  >3. **`name`:**
  >   - The name of the process or the path to the program.
  >   - For example, `/proc/boot/procnto-smp-instr` is the microkernel process.
  >4. **`prio` (Priority):**
  >   - The scheduling priority of the thread.
  >   - Lower values indicate higher priority, and higher values indicate lower priority.
  >   - The suffix (e.g., `f`, `r`, or `i`) indicates special states:
  >     - `f`: FIFO scheduling (fixed priority).
  >     - `r`: Round-robin scheduling.
  >     - `i`: Interrupt handler.
  >5. **`STATE`:**
  >   - The current state of the thread:
  >     - `RUNNING`: The thread is executing on the CPU.
  >     - `READY`: The thread is ready to run but waiting for the CPU.
  >     - `RECEIVE`: The thread is waiting to receive a message.
  >     - `REPLY`: The thread is waiting for a reply to a sent message.
  >     - `NANOSLEEP`: The thread is sleeping for a short period.
  >     - `SIGWAITINFO`: The thread is waiting for a signal.
  >     - `CONDVAR`: The thread is waiting on a condition variable.
  >     - `SEM`: The thread is waiting on a semaphore.
  >6. **`Blocked`:**
  >   - If the thread is in a blocked state (e.g., `RECEIVE`, `REPLY`, or `CONDVAR`), this column shows the reason or the object it is waiting on:
  >     - `1`: Waiting for a specific process or thread.
  >     - `(0x0)`: Waiting on a memory object or condition variable.

- **States of Processes**:

  - **READY**: Process is ready to execute.
  - **BLOCKED**: Waiting for an event or resource.
  - **RUNNING**: Actively executing on the CPU.

- **Examples**

>#### **Line:**
>
>```bash
>1   1 /proc/boot/procnto-smp-instr   0f RUNNING
>```
>
>- `pid`: `1` → Process ID of the microkernel (`/proc/boot/procnto-smp-instr`).
>- `tid`: `1` → First thread of this process.
>- `name`: `/proc/boot/procnto-smp-instr` → Name of the microkernel process.
>- `prio`: `0f` → Fixed-priority thread (`f` = FIFO scheduling).
>- `STATE`: `RUNNING` → The thread is actively running.
>
>#### **Line:**
>
>```
>1  13 /proc/boot/procnto-smp-instr   1f NANOSLEEP
>```
>
>- `pid`: `1` → Microkernel process.
>- `tid`: `13` → Thread within the microkernel.
>- `prio`: `1f` → FIFO scheduling with priority `1`.
>- `STATE`: `NANOSLEEP` → The thread is temporarily sleeping.
>
>#### **Line:**
>
>```bash
>24580   1 proc/boot/devc-serminiuart    10r RECEIVE        1
>```
>
>- `pid`: `24580` → Process ID of the `devc-serminiuart` device driver.
>- `tid`: `1` → Main thread of this process.
>- `prio`: `10r` → Round-robin scheduling with priority `10`.
>- `STATE`: `RECEIVE` → Waiting to receive a message.
>- `Blocked`: `1` → Waiting for a message from process `1` (likely the microkernel).
>
>#### **Line:**
>
>```bash
>241677  20 system/bin/io-sock            10r CONDVAR        (0x0)
>```
>
>- `pid`: `241677` → Process ID of the `io-sock` process.
>- `tid`: `20` → Thread within this process.
>- `prio`: `10r` → Round-robin scheduling with priority `10`.
>- `STATE`: `CONDVAR` → Waiting on a condition variable.
>- `Blocked`: `(0x0)` → Waiting on a condition variable object at memory location `0x0`.
>
>--------------------------

- **Microkernel (procnto-smp-instr):**

  - `pid` = `1` → This is the main process hosting the QNX Neutrino microkernel.

  - Has multiple threads handling different tasks, such as:
    - Interrupts (`INTR`).
    - Message passing (`RECEIVE`).
    - Timing operations (`NANOSLEEP`).

- **Device Drivers:**

  - Processes like `devc-serminiuart` represent device drivers for serial communication.

  - They often wait in the `RECEIVE` state, ready to handle hardware or kernel messages.

- **System Services:**

  - Processes like `slogger2` handle logging.

  - Often blocked in states like `RECEIVE`, waiting for messages or signals from other processes.

- **Application Threads:**
  - Threads in the `io-sock` process are waiting on condition variables or semaphores for events like socket I/O.

-------------------

**Example**

```
692246   3 proc/boot/io-usb-otg          10r CONDVAR        (0x0)
```

1. **`pid` (Process ID):**
   - `692246`: This is the unique ID of the process running the `io-usb-otg` executable.
   - The `io-usb-otg` process is the USB On-The-Go (OTG) service, responsible for USB device handling.
2. **`tid` (Thread ID):**
   - `3`: The thread ID within the `io-usb-otg` process. This is the third thread of the process.
3. **`name`:**
   - `proc/boot/io-usb-otg`: The executable name or path for the USB OTG service.
4. **`prio` (Priority):**
   - `10`: The thread’s scheduling priority is 10.
   - Lower-priority numbers represent higher-priority threads. A value of `10` indicates a moderate priority.
5. **`STATE`:**
   - `CONDVAR`: The thread is currently blocked and waiting on a **condition variable**.
   - A condition variable is a synchronization primitive used to coordinate thread execution. The thread is likely waiting for a signal or notification from another thread to proceed.
6. **`Blocked`:**
   - `(0x0)`: Indicates the thread is waiting on a condition variable located at virtual address `0x0`.
   - Normally, the address here corresponds to the location of the condition variable in memory.
   - In your case, `0x0` means:
     - Either the condition variable hasn’t been properly initialized.
     - Or, it is waiting for a generic synchronization object not tied to a specific address.
