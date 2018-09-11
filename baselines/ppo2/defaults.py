def mujoco():
    return dict(
        nsteps=2048,
        nminibatches=32,
        lam=0.95,
        gamma=0.99,
        noptepochs=10,
        log_interval=1,
        ent_coef=0.0,
        lr=lambda f: 3e-4 * f,
        cliprange=0.2,
        value_network='copy'
    )

def atari():
    return dict(
        nsteps=128, 
        nminibatches=4,
        lam=0.95, 
        gamma=0.99, 
        noptepochs=4, 
        log_interval=1,
        ent_coef=.01,
        lr=lambda f : f * 2.5e-4,
        cliprange=lambda f : f * 0.1,
    )

def airhockey():
    return dict(
        nsteps=2048,
        nminibatches=256,
        lam=0.5**(1./8),
        gamma=0.5**(1./16), # half value after 16 steps
        noptepochs=10,
        log_interval=1,
        ent_coef=0.0,
        lr=lambda f: 7e-4 * f,
        cliprange=lambda f: f * 0.15 + 0.05,
        value_network='copy'
    )