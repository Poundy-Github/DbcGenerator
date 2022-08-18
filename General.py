from signal import signal
import canmatrix
import pylightxl
import decimal


def GeneralAttributeAdd(matrix: canmatrix.CanMatrix,demo_matrix: canmatrix.CanMatrix):
    # if demo_matrix == None:
    #     # Db attr defines
    #     matrix.add_global_defines("DBName", 'STRING')
    #     matrix.add_define_default("DBName", dbName)
    #     matrix.add_attribute("DBName", dbName)
    #
    #     # msg attr defines
    #     matrix.add_frame_defines("GenMsgCycleTime", 'INT 0 65535')
    #     matrix.add_define_default("GenMsgCycleTime", "0")
    #
    #     matrix.add_frame_defines("GenMsgDelayTime", 'INT 0 65535')
    #     matrix.add_define_default("GenMsgDelayTime", "0")
    #
    #     matrix.add_frame_defines("GenMsgNrOfRepetition", 'INT 0 65535')
    #     matrix.add_define_default("GenMsgNrOfRepetition", "0")
    #
    #     matrix.add_frame_defines("GenMsgCycleTimeFast", 'INT 0 65535')
    #     matrix.add_define_default("GenMsgCycleTimeFast", "0")
    #
    #     matrix.add_frame_defines("GenMsgSendType", 'ENUM  "Cyclic","CyclicAndSpontanX","Event"')
    #     matrix.add_define_default("GenMsgSendType", "Cyclic")
    #
    #     matrix.add_frame_defines("GenMsgILSupport", 'ENUM  "No", "Yes"')
    #     matrix.add_define_default("GenMsgILSupport", "Yes")
    #
    #     matrix.add_signal_defines("GenSigSendType",
    #                               'ENUM  "Cyclic","OnWrite","OnWriteWithRepetition","OnChange","OnChangeWithRepetition","NotUsed","NotUsed","NoSigSendType"')
    #     matrix.add_define_default("GenSigSendType", "Cyclic")
    #
    #     # signal attr defines
    #     matrix.add_signal_defines("GenSigCycleTime", 'INT 0 65535')
    #     matrix.add_define_default("GenSigCycleTime", "0")
    #
    #     matrix.add_signal_defines("GenSigSendType",
    #                               'ENUM  "Cyclic","OnWrite","OnWriteWithRepetition","OnChange","OnChangeWithRepetition","IfActive","IfActiveWithRepetition","NoSigSendType","NotUsed","NotUsed","NotUsed","NotUsed","NotUsed"')
    #     matrix.add_define_default("GenSigSendType", "Cyclic")
    # else:

    matrix.global_defines = demo_matrix.global_defines
    matrix.ecu_defines = demo_matrix.ecu_defines
    matrix.frame_defines = demo_matrix.frame_defines
    matrix.signal_defines = demo_matrix.signal_defines
    matrix.env_defines = demo_matrix.env_defines


def CreatCanFrame(dbc, comSheet, is_fd, data_row, data_cfg) -> canmatrix.Frame:
    if data_row <= 0 or data_cfg == None:
        return None

    frame = canmatrix.Frame()

    frame.name = str(comSheet.index(row=data_row, col=data_cfg['frameName'])).strip(' ')
    frame.add_comment(comSheet.index(row=data_row, col=data_cfg['comment']))
    frame.is_fd = is_fd

    sender_string = str(comSheet.index(row=data_row, col=data_cfg['sendNode'])).strip(' ')
    if sender_string != None:
        frame.add_transmitter(sender_string)

    # attributes
    frame.add_attribute("GenMsgCycleTime", str(comSheet.index(row=data_row, col=data_cfg['circle'])).strip(' '))
    frame.add_attribute("GenMsgILSupport", "Yes")
    # transmmit type  TODO
    frame.add_attribute("GenMsgSendType", "Cyclic")

    # # frame size TODO
    frame.size = 64
    # # frame.fit_dlc()

    try:
        id_str = str(comSheet.index(row=data_row, col=data_cfg['id']))
        frame.arbitration_id.id = int(id_str, 16)
    except:
        print('can id format error !')

    return frame


def CreateCanSignal(frame, comSheet, row, data_cfg, ecu_list) -> canmatrix.Signal:
    # signal info -- frame --- ecu
    signal = canmatrix.Signal()
    signal.name = str(comSheet.index(row=row, col=data_cfg['signalName'])).strip()
    # receivers 
    receivers = str(comSheet.index(row=row, col=data_cfg['recvNode'])).strip().split(',')
    senders = str(comSheet.index(row=row, col=data_cfg['sendNode'])).strip().split(',')

    if receivers != None and senders != None:
        for receiver in receivers:
            signal.add_receiver(receiver)
            frame.add_receiver(receiver)
            if receiver not in ecu_list:
                ecu_list.append(receiver)

    # signal send type TODO 
    # signal.add_attribute()
    # try:
    sb_str = str(comSheet.index(row=row, col=data_cfg['signal_start_bit'])).strip()
    sb = int(sb_str, 10)
    len_str = str(comSheet.index(row=row, col=data_cfg['signal_length'])).strip()
    len = int(len_str, 10)
    data_type = str(comSheet.index(row=row, col=data_cfg['signalType'])).strip()
    physicalMin_str = str(comSheet.index(row=row, col=data_cfg['physicalMin'])).strip()
    physicalMin = decimal.Decimal(physicalMin_str)
    physicalMax_str = str(comSheet.index(row=row, col=data_cfg['physicalMax'])).strip()
    physicalMax = decimal.Decimal(physicalMax_str)
    factor_str = str(comSheet.index(row=row, col=data_cfg['factor'])).strip()
    factor = decimal.Decimal(factor_str)
    offset_str = str(comSheet.index(row=row, col=data_cfg['offset'])).strip()
    offset = decimal.Decimal(offset_str)

    initVal_str = str(comSheet.index(row=row, col=data_cfg['initVal'])).strip()
    try:
        initVal = decimal.Decimal(initVal_str)
    except:
        initVal = decimal.Decimal('0')
    comment = str(comSheet.index(row=row, col=data_cfg['comment'])).encode("GBK")
    unit = str(comSheet.index(row=row, col=data_cfg['unit']))

    signal.unit = unit
    # signal.add_comment(comment)
    signal.comment = comment.decode('GBK')

    # TODO phys2raw error
    signal.factor = factor
    signal.set_max(physicalMax)
    signal.set_min(physicalMin)
    signal.offset = offset

    signal.start_bit = sb
    signal.size = len
    signal.initial_value = initVal
    # data type
    if data_type.lower() == 'signed':
        signal.is_signed = True
        signal.is_float = False
    elif data_type.lower() == "float":
        signal.is_signed = False
        signal.is_float = True
    else:
        signal.is_signed = False
        signal.is_float = False

    return signal
