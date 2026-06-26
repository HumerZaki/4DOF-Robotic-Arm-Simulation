from tkinter import *
import math

# --- Window setup ---
window = Tk()
window.title("4-DOF Robotic Arm Simulator (Shoulder-Based)")
window.geometry("900x500")
window.config(bg="lightgray")

# --- Canvas setup ---
canvas = Canvas(window, bg="lightyellow", width=900, height=400)
canvas.pack(pady=10)

# --- Arm link lengths ---
L1 = 100  # Shoulder link (base to elbow)
L2 = 80   # Elbow link (forearm)
L3 = 60   # Wrist link
L4 = 40   # Tool/Hand link

# --- Base (shoulder) position ---
base_x, base_y = 450, 380  # ground point

# --- Draw arm ---
def draw_arm(theta1, theta2, theta3, theta4):
    canvas.delete("all")

    # Convert to radians
    t1 = math.radians(theta1)
    t2 = math.radians(theta2)
    t3 = math.radians(theta3)
    t4 = math.radians(theta4)

    # Calculate joint positions
    x1 = base_x + L1 * math.cos(t1)
    y1 = base_y - L1 * math.sin(t1)

    x2 = x1 + L2 * math.cos(t1 + t2)
    y2 = y1 - L2 * math.sin(t1 + t2)

    x3 = x2 + L3 * math.cos(t1 + t2 + t3)
    y3 = y2 - L3 * math.sin(t1 + t2 + t3)

    x4 = x3 + L4 * math.cos(t1 + t2 + t3 + t4)
    y4 = y3 - L4 * math.sin(t1 + t2 + t3 + t4)

    # --- Draw base ---
    canvas.create_rectangle(base_x - 40, base_y, base_x + 40, base_y + 20, fill="black")

    # --- Draw links ---
    canvas.create_line(base_x, base_y, x1, y1, width=6, fill="red")
    canvas.create_line(x1, y1, x2, y2, width=6, fill="blue")
    canvas.create_line(x2, y2, x3, y3, width=6, fill="green")
    canvas.create_line(x3, y3, x4, y4, width=4, fill="purple")

    # --- Draw joints ---
    for (x, y) in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")

    # --- Info text ---
    canvas.create_text(150, 20, text=f"End Effector: ({x4:.1f}, {y4:.1f})", font=("Arial", 12))
    canvas.create_text(180, 40, text=f"θ₁={theta1}°, θ₂={theta2}°, θ₃={theta3}°, θ₄={theta4}°", font=("Arial", 10))

# --- Slider update ---
def update_arm(event=None):
    t1 = slider1.get()
    t2 = slider2.get()
    t3 = slider3.get()
    t4 = slider4.get()
    draw_arm(t1, t2, t3, t4)

# --- Control sliders ---
Label(window, text="Shoulder Joint (θ₁)", bg="lightgray").pack()
slider1 = Scale(window, from_=0, to=180, orient=HORIZONTAL, length=500, command=update_arm)
slider1.set(45)
slider1.pack()

Label(window, text="Elbow Joint (θ₂)", bg="lightgray").pack()
slider2 = Scale(window, from_=-135, to=135, orient=HORIZONTAL, length=500, command=update_arm)
slider2.set(30)
slider2.pack()

Label(window, text="Wrist Joint (θ₃)", bg="lightgray").pack()
slider3 = Scale(window, from_=-90, to=90, orient=HORIZONTAL, length=500, command=update_arm)
slider3.set(0)
slider3.pack()

Label(window, text="Tool/Hand Joint (θ₄)", bg="lightgray").pack()
slider4 = Scale(window, from_=-90, to=90, orient=HORIZONTAL, length=500, command=update_arm)
slider4.set(0)
slider4.pack()

# --- Initial draw ---
draw_arm(45, 30, 0, 0)

window.mainloop()
