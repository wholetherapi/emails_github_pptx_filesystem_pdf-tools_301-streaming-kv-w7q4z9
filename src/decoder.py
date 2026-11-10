"""Memory-bounded decoding loop."""


def decode_step(model, state, token):
    return model.forward(state, token)
