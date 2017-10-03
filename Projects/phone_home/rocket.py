def numerical():
    from scipy.integrate import odeint
    from numpy import array

    # [position, mass, velocity, mass flow]

    def acceleration(y, t, v_exhaust=1.0):
        return array([y[2], y[3], v_exhaust * y[3]/y[1], 0.0])

    initial_state = array([0.0, 2.0, 0.0, -1.0])
    solution = odeint(acceleration, initial_state, [i/10.0 for i in range(11)], args=(1.0,))

    print(solution)

numerical()
