from manim import *
import numpy as np

class PendulumScene(Scene):
    def construct(self):
        # Parameters
        length = 2.5
        g = 9.81
        mass = 1.5
        theta_0 = 179 * DEGREES
        omega_0 = 0         # Initial angular velocity
        
        dt = 0.02
        total_time = 25
        
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_tip": False}
        )
        
        # Pendulum
        origin = Dot(ORIGIN, color=RED)
        origin_label = Text("O").next_to(origin, UP+LEFT, buff=0.2)
        
        initial_pos = np.array([length * np.sin(theta_0), -length * np.cos(theta_0), 0])
        bob = Dot(initial_pos, color=BLUE).scale(1.5)
        rod = Line(origin.get_center(), bob.get_center(), color=WHITE)
        
        # Force vectors
        force_scale = 0.1
        weight = Arrow(
            bob.get_center(), 
            bob.get_center() + np.array([0, -mass*g*force_scale, 0]),
            buff=0, 
            color=RED
        )
        
        r_direction = normalize(initial_pos - ORIGIN)
        theta_hat = np.array([-r_direction[1], r_direction[0], 0])

        tension_magnitude = max(mass * g * np.cos(theta_0), 0)
        tension_vector = -r_direction * tension_magnitude * force_scale
        tension = Arrow(
            bob.get_center(),
            bob.get_center() + tension_vector,
            buff=0,
            color=BLUE
        )

        a_tangential = -g * np.sin(theta_0)
        a_centripetal = -length * omega_0**2
        total_accel_vector = (a_tangential * theta_hat + a_centripetal * r_direction) * force_scale
        total_accel = Arrow(
            bob.get_center(),
            bob.get_center() + total_accel_vector,
            buff=0,
            color=PURPLE
        )
        
        angle_arc = Arc(radius=0.8, start_angle=-PI/2, angle=theta_0, color=WHITE)
        angle_label = MathTex("\\theta").next_to(angle_arc, RIGHT, buff=0.2)
        
        weight_label = MathTex("mg", color=RED).add_updater(
            lambda m: m.next_to(weight.get_end(), RIGHT, buff=0.1)
        )
        tension_label = MathTex("T", color=BLUE).add_updater(
            lambda m: m.next_to(tension.get_end(), 
                               UP if tension.get_length() > 0.1 else DOWN,
                               buff=0.1)
        )
        accel_label = MathTex("a", color=PURPLE).add_updater(
            lambda m: m.next_to(total_accel.get_end(), 
                               RIGHT if total_accel.get_end()[0] > bob.get_center()[0] else LEFT, 
                               buff=0.1)
        )
        
        pendulum = VGroup(
            origin, origin_label, rod, bob,
            weight, tension, total_accel,
            weight_label, tension_label, accel_label,
            angle_arc, angle_label
        )
        
        self.add(axes, pendulum)
        
        title = Text("Pendulum Forces and Acceleration").to_edge(UP, buff=0.5)
        self.add(title)
        
        theta = theta_0
        omega = omega_0
        
        def update_pendulum(mob, dt):
            nonlocal theta, omega
            
            alpha = -g / length * np.sin(theta)
            omega += alpha * dt
            theta += omega * dt
            
            new_x = length * np.sin(theta)
            new_y = -length * np.cos(theta)
            new_position = np.array([new_x, new_y, 0])
            
            mob[2].put_start_and_end_on(ORIGIN, new_position)
            mob[3].move_to(new_position)
            
            r_direction = normalize(new_position - ORIGIN)
            theta_hat = np.array([-r_direction[1], r_direction[0], 0])
            
            mob[4].put_start_and_end_on(
                new_position,
                new_position + np.array([0, -mass*g*force_scale, 0])
            )
            
            tension_magnitude = mass * (g * np.cos(theta) + length * omega**2)
            tension_magnitude = max(tension_magnitude, 0)
            tension_vector = -r_direction * tension_magnitude * force_scale
            mob[5].put_start_and_end_on(
                new_position,
                new_position + tension_vector
            )
            
            # Total acceleration
            a_tangential = -g * np.sin(theta)
            a_centripetal = -length * omega**2
            total_accel_vector = (a_tangential * theta_hat + a_centripetal * r_direction) * force_scale
            mob[6].put_start_and_end_on(
                new_position,
                new_position + total_accel_vector
            )
            
            new_angle = abs(theta)
            mob[10].become(
                Arc(radius=0.8, 
                    start_angle=-PI/2, 
                    angle=new_angle if theta > 0 else -new_angle, 
                    color=WHITE)
            )
            mob[11].next_to(mob[10], 
                            RIGHT if abs(theta) > PI/4 else UP, 
                            buff=0.2)
        
        self.play(
            UpdateFromAlphaFunc(
                pendulum,
                lambda mob, alpha: update_pendulum(mob, dt),
                run_time=total_time,
                rate_func=linear
            )
        )
        
        self.wait(1)

if __name__ == "__main__":
    pass