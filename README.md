# PINNs-course
Material to learn about Physics-informed neural networks (PINNs), a machine learning technique that combines neural networks with physical insights. PINNs are particularly useful for solving physics and engineering problems with limited or expensive data.


# Installation

We recommend setting up a new Python environment. You can do this by running the following commands:

 ```
 conda create --name pinns-course-env
 conda activate pinns-course-env
 ```

Next, clone this repository by using the command:

 ```
git clone https://github.com/oscar-rincon/PINNs-course.git
 ```

Finally, go to the `PINNs-course/` folder and run the following command to install the necessary dependencies:

 ```
 conda env update --name pinns-course-env --file pinns_course_env.yaml
 ```

To verify the packages installed in your `pinns-course-env` conda environment, you can use the following command:

 ```
 conda list -n pinns-course-env
 ```