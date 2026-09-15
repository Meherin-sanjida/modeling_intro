import numpy as np
import matplotlib.pyplot as plt


def point_in_triangle(point, vertex_a, vertex_b, vertex_c):

    vector_0 = vertex_c - vertex_a
    vector_1 = vertex_b - vertex_a
    vector_2 = point - vertex_a

    dot_00 = np.dot(vector_0, vector_0)
    dot_01 = np.dot(vector_0, vector_1)
    dot_02 = np.dot(vector_0, vector_2)
    dot_11 = np.dot(vector_1, vector_1)
    dot_12 = np.dot(vector_1, vector_2)

    denominator = dot_00 * dot_11 - dot_01 * dot_01

    u = (dot_11 * dot_02 - dot_01 * dot_12) / denominator
    v = (dot_00 * dot_12 - dot_01 * dot_02) / denominator

    return (u >= 0) and (v >= 0) and (u + v <= 1)


def generate_rgb_triangle(width=800, height=700, border=100):
    

    # Create a white RGB image
    image = np.ones((height, width, 3), dtype=float)

    # Define the three triangle vertices
    red_vertex = np.array([
        width / 2,
        border
    ])

    green_vertex = np.array([
        border,
        height - border
    ])

    blue_vertex = np.array([
        width - border,
        height - border
    ])

    # Find the largest distance between any two vertices
    max_distance = max(
        np.linalg.norm(red_vertex - green_vertex),
        np.linalg.norm(red_vertex - blue_vertex),
        np.linalg.norm(green_vertex - blue_vertex)
    )

    # Calculate the RGB value for each pixel
    for y_coordinate in range(height):

        for x_coordinate in range(width):

            pixel = np.array([
                x_coordinate,
                y_coordinate
            ])

            # Only assign RGB colors to points inside the triangle
            if point_in_triangle(
                pixel,
                red_vertex,
                green_vertex,
                blue_vertex
            ):

                # Calculate distance from the pixel to each vertex
                distance_to_red = np.linalg.norm(
                    pixel - red_vertex
                )

                distance_to_green = np.linalg.norm(
                    pixel - green_vertex
                )

                distance_to_blue = np.linalg.norm(
                    pixel - blue_vertex
                )

                # Convert distance to RGB intensity
                red_value = 1.0 - distance_to_red / max_distance
                green_value = 1.0 - distance_to_green / max_distance
                blue_value = 1.0 - distance_to_blue / max_distance

                pixel_color = np.array([
                    red_value,
                    green_value,
                    blue_value
                ])

                # Normalize colors to keep them vivid
                pixel_color = pixel_color / pixel_color.max()

                # Assign the calculated RGB color to the pixel
                image[
                    y_coordinate,
                    x_coordinate
                ] = pixel_color

    return (
        image,
        red_vertex,
        green_vertex,
        blue_vertex
    )


def display_project_on_triangle(
    image,
    project_x,
    project_y,
    point_color="black",
    point_size=150,
    point_marker="o",
    save=False,
    filename="research_triangle.png"
):
    
    # Create the figure
    plt.figure(figsize=(8, 7))

    # Display the RGB triangle
    plt.imshow(image)

    # Add the research project point
    plt.scatter(
        project_x,
        project_y,
        color=point_color,
        s=point_size,
        marker=point_marker,
        label="research project"
    )

    # Add labels identifying the three research approaches
    plt.text(
        image.shape[1] / 2,
        70,
        "analytical",
        ha="center",
        fontsize=12
    )

    plt.text(
        70,
        image.shape[0] - 50,
        "physical",
        ha="center",
        fontsize=12
    )

    plt.text(
        image.shape[1] - 70,
        image.shape[0] - 50,
        "data driven",
        ha="center",
        fontsize=12
    )

    plt.legend()

    # Hide x- and y-axis
    plt.axis("off")

    # Save the figure only when requested
    if save:
        plt.savefig(
            filename,
            dpi=300,
            bbox_inches="tight"
        )

    # Display the completed figure
    plt.show()


# ---------------------------------------------------------
# Generate the RGB triangle
# ---------------------------------------------------------

triangle_image, red_vertex, green_vertex, blue_vertex = generate_rgb_triangle(
    width=800,
    height=700,
    border=100
)


# ---------------------------------------------------------
# Add the location of your research project
# ---------------------------------------------------------

display_project_on_triangle(
    triangle_image,
    project_x=400,
    project_y=400,
    point_color="blue",
    point_size=100,
    point_marker="o",
    save=False
)