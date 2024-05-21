from tlib.ml import make_model_with_scalar_input_single_hidden_fc
from tlib.ml.input import MNIST10Input
from tlib.ml.base import StepDecay, model_auto_saver
from keras.models import Model
from keras.optimizers import Adam


def main():

    model_name = "mnist10"
    ipt_mgr = MNIST10Input()
    ipt_mgr.process()

    m: Model = make_model_with_scalar_input_single_hidden_fc(
        input_shape=[28 * 28,],
        num_neurons_in_hidden_layer=256,
        num_output=10,
        hidden_layer_activation='relu',
        output_layer_activiation='softmax'
    )
    opt = Adam()
    step_decay = StepDecay(init_r=0.001, drop=0.5, epochs_per_step=10)
    lr_sched = step_decay.step_decay()
    m.compile(
        optimizer=opt,
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    m.summary()

    m.fit(
        ipt_mgr.x_train,
        ipt_mgr.y_train,
        batch_size=128,
        validation_split=0.2,
        epochs=30,
        callbacks=[lr_sched, model_auto_saver(model_name)]
    )
    score = m.evaluate(ipt_mgr.x_test, ipt_mgr.y_test)
    print(score)


if __name__ == "__main__":
    main()
